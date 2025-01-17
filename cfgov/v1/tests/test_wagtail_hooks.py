from django.contrib.auth.models import Permission, User
from django.core.exceptions import PermissionDenied
from django.test import RequestFactory, SimpleTestCase, TestCase
from django.urls import reverse

from wagtail import hooks
from wagtail.admin.views.pages.bulk_actions.delete import DeleteBulkAction
from wagtail.admin.views.pages.delete import delete
from wagtail.models import Page
from wagtail.test.utils import WagtailTestUtils
from wagtail.whitelist import Whitelister as Allowlister

from v1.models import BlogPage, CFGOVPageCategory, InternalDocsSettings
from v1.tests.wagtail_pages.helpers import publish_page
from v1.wagtail_hooks import raise_bulk_delete_error, raise_delete_error


class TestAllowlistOverride(SimpleTestCase):
    # Borrowed from https://github.com/wagtail/wagtail/blob/master/wagtail
    # /core/tests/test_whitelist.py

    def setUp(self):
        self.allowlister = Allowlister()

    def test_allowlist_hooks(self):
        """
        Allowlister.clean should remove disallowed tags and attributes from
        a string
        """
        input_html = '<scan class="id">Consumer <embed>Finance</embed></scan>'
        output_html = self.allowlister.clean(input_html)
        self.assertHTMLEqual(output_html, "Consumer Finance")


class TestDeleteProtections(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            email="test@cfpb.gov",
            password="test",
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        self.page1 = BlogPage(title="live1", slug="test1")
        self.page1.categories.add(CFGOVPageCategory(name="foo"))
        self.page1.tags.add("foo")
        self.page1.authors.add("test-author")
        self.page1.language = "en"
        self.page2 = BlogPage(title="live2", slug="test2")
        self.page2.categories.add(CFGOVPageCategory(name="bar"))
        self.page2.tags.add("bar")
        self.page2.authors.add("test-author")
        self.page2.language = "en"
        publish_page(self.page1)
        publish_page(self.page2)
        self.request = RequestFactory().post(
            f"/admin/bulk/wagtailcore/page/delete/"
            f"?next=%2Fadmin%2Fpages%2F3%2F&"
            f"id={self.page1.pk}&id={self.page2.pk}"
        )
        self.request.user = self.user

    @hooks.register_temporarily("before_delete_page", raise_delete_error)
    def test_delete_page_block(self):
        """
        Test Page Deletion Protections via proper hook and hook calling method.
        Page delete method requires a request just to pull a user with valid
        permissions to check, so URL is no factor. Even with valid permissions
        this should raise PermissionDenied.
        """
        self.assertRaises(
            PermissionDenied, delete, self.request, self.page1.pk
        )

    @hooks.register_temporarily("before_bulk_action", raise_bulk_delete_error)
    def test_bulk_delete_block(self):
        """
        Test Bulk Delete Protections via proper hook and hook calling method.
        Action requires a request with a user with valid permissions, as well
        as a bulk delete URL with parsable valid object id's.
        URL determines the action type and object type.
        form_valid is what ultimately calls before and after hooks for all
        bulk actions. form_valid does not, however, require a valid
        form object, so None is passed.
        We test with Pages here, but the method should protect against all
        object bulk deletion. Even with valid permissions this should raise
        PermissionDenied.
        """
        action = DeleteBulkAction(self.request, model=Page)
        self.assertRaises(
            PermissionDenied,
            action.form_valid,
            None,
        )


class TestDjangoAdminLink(TestCase, WagtailTestUtils):
    def get_admin_response_for_user(self, is_staff):
        credentials = {"username": "regular", "password": "regular"}
        user = self.create_user(is_staff=is_staff, **credentials)

        user.user_permissions.add(
            Permission.objects.get(
                content_type__app_label="wagtailadmin", codename="access_admin"
            )
        )
        user.save()

        self.login(**credentials)
        return self.client.get(reverse("wagtailadmin_home"))

    def test_staff_sees_django_admin_link(self):
        response = self.get_admin_response_for_user(is_staff=True)
        self.assertContains(response, "Django Admin")

    def test_non_staff_doesnt_see_django_admin_link(self):
        response = self.get_admin_response_for_user(is_staff=False)
        self.assertNotContains(response, "Django Admin")


class TestInternalDocsLink(TestCase, WagtailTestUtils):
    def setUp(self):
        self.login()

    def get_admin_response(self):
        return self.client.get(reverse("wagtailadmin_home"))

    def test_docs_not_defined_no_link_in_admin(self):
        self.assertNotContains(
            self.get_admin_response(), "/admin/internal-docs/"
        )

    def test_guide_defined_creates_link_in_admin(self):
        InternalDocsSettings.objects.create(url="https://example.com/")
        self.assertContains(self.get_admin_response(), "/admin/internal-docs/")
