# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks
import v1.atomic_elements.organisms


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0034_add_story_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browsefilterablepage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField([(b'full_width_text', wagtail.wagtailcore.blocks.StreamBlock([(b'content_with_anchor', wagtail.wagtailcore.blocks.StructBlock([(b'content_block', wagtail.wagtailcore.blocks.RichTextBlock()), (b'anchor_link', wagtail.wagtailcore.blocks.StructBlock([(b'link_id', wagtail.wagtailcore.blocks.CharBlock(help_text=(b'Auto-generated on save, or enter some human-friendly text ', b'to make it easier to read.'), required=False, label=b'ID for this content block'))]))])), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'media', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'body', wagtail.wagtailcore.blocks.TextBlock()), (b'citation', wagtail.wagtailcore.blocks.TextBlock())])), (b'cta', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))])), (b'related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock())), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock()), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))], editable=False)), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'}))])), (b'filter_controls', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'is_bordered', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_midtone', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_expanded', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'form_type', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'filterable-list', choices=[(b'filterable-list', b'Filterable List'), (b'pdf-generator', b'PDF Generator')])), (b'title', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Filter Title')), (b'post_date_description', wagtail.wagtailcore.blocks.CharBlock(default=b'Published')), (b'categories', wagtail.wagtailcore.blocks.StructBlock([(b'filter_category', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False)), (b'show_preview_categories', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False)), (b'page_type', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=[(b'activity-log', b'Activity Log'), (b'amicus-brief', b'Amicus Brief'), (b'blog', b'Blog'), (b'enforcement', b'Enforcement Action'), (b'final-rule', b'Final Rule'), (b'foia-freq-req-record', b'FOIA Frequently Requested Record'), (b'impl-resource', b'Implementation Resource'), (b'leadership-calendar', b'Leadership Calendar'), (b'newsroom', b'Newsroom'), (b'notice-opportunity-comment', b'Notice and Opportunity for Comment'), (b'research-reports', b'Research Report'), (b'rule-under-dev', b'Rule Under Development'), (b'story', b'Story')]))])), (b'topics', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Filter Topics')), (b'authors', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Filter Authors')), (b'date_range', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Filter Date Range')), (b'output_5050', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Render preview items as 50-50s'))])), (b'feedback', wagtail.wagtailcore.blocks.StructBlock([(b'was_it_helpful_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Use this field only for feedback forms that use "Was this helpful?" radio buttons.', default=b'Was this page helpful to you?', required=False)), (b'intro_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional feedback intro', required=False)), (b'question_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional expansion on intro', required=False)), (b'radio_intro', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Leave blank unless you are building a feedback form with extra radio-button prompts, as in /owning-a-home/help-us-improve/.', required=False)), (b'radio_text', wagtail.wagtailcore.blocks.CharBlock(default=b'This information helps us understand your question better.', required=False)), (b'radio_question_1', wagtail.wagtailcore.blocks.CharBlock(default=b'How soon do you expect to buy a home?', required=False)), (b'radio_question_2', wagtail.wagtailcore.blocks.CharBlock(default=b'Do you currently own a home?', required=False)), (b'button_text', wagtail.wagtailcore.blocks.CharBlock(default=b'Submit')), (b'contact_advisory', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Use only for feedback forms that ask for a contact email', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='sublandingfilterablepage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField([(b'text_introduction', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), (b'full_width_text', wagtail.wagtailcore.blocks.StreamBlock([(b'content_with_anchor', wagtail.wagtailcore.blocks.StructBlock([(b'content_block', wagtail.wagtailcore.blocks.RichTextBlock()), (b'anchor_link', wagtail.wagtailcore.blocks.StructBlock([(b'link_id', wagtail.wagtailcore.blocks.CharBlock(help_text=(b'Auto-generated on save, or enter some human-friendly text ', b'to make it easier to read.'), required=False, label=b'ID for this content block'))]))])), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'media', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'body', wagtail.wagtailcore.blocks.TextBlock()), (b'citation', wagtail.wagtailcore.blocks.TextBlock())])), (b'cta', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))])), (b'related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock())), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock()), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))], editable=False)), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'}))])), (b'filter_controls', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'is_bordered', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_midtone', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_expanded', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'form_type', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'filterable-list', choices=[(b'filterable-list', b'Filterable List'), (b'pdf-generator', b'PDF Generator')])), (b'title', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Filter Title')), (b'post_date_description', wagtail.wagtailcore.blocks.CharBlock(default=b'Published')), (b'categories', wagtail.wagtailcore.blocks.StructBlock([(b'filter_category', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False)), (b'show_preview_categories', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False)), (b'page_type', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=[(b'activity-log', b'Activity Log'), (b'amicus-brief', b'Amicus Brief'), (b'blog', b'Blog'), (b'enforcement', b'Enforcement Action'), (b'final-rule', b'Final Rule'), (b'foia-freq-req-record', b'FOIA Frequently Requested Record'), (b'impl-resource', b'Implementation Resource'), (b'leadership-calendar', b'Leadership Calendar'), (b'newsroom', b'Newsroom'), (b'notice-opportunity-comment', b'Notice and Opportunity for Comment'), (b'research-reports', b'Research Report'), (b'rule-under-dev', b'Rule Under Development'), (b'story', b'Story')]))])), (b'topics', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Filter Topics')), (b'authors', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Filter Authors')), (b'date_range', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False, label=b'Filter Date Range')), (b'output_5050', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Render preview items as 50-50s'))])), (b'featured_content', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'category', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, choices=[(b'featured-event', b'Featured event'), (b'featured-blog', b'Featured blog'), (b'featured-video', b'Featured video'), (b'featured-tool', b'Featured tool'), (b'featured-news', b'Featured news'), (b'featured', b'Featured')])), (b'post', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), (b'show_post_link', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Render post link?')), (b'post_link_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), label=b'Additional Links')), (b'video', wagtail.wagtailcore.blocks.StructBlock([(b'id', wagtail.wagtailcore.blocks.CharBlock(help_text=b'E.g., in "https://www.youtube.com/watch?v=en0Iq8II4fA", the ID is everything after the "?v=".', required=False, label=b'ID')), (b'url', wagtail.wagtailcore.blocks.CharBlock(help_text=b'You must use the embed URL, e.g., https://www.youtube.com/embed/JPTg8ZB3j5c?autoplay=1&enablejsapi=1', required=False, label=b'URL')), (b'height', wagtail.wagtailcore.blocks.CharBlock(default=b'320', required=False)), (b'width', wagtail.wagtailcore.blocks.CharBlock(default=b'568', required=False))]))])), (b'feedback', wagtail.wagtailcore.blocks.StructBlock([(b'was_it_helpful_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Use this field only for feedback forms that use "Was this helpful?" radio buttons.', default=b'Was this page helpful to you?', required=False)), (b'intro_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional feedback intro', required=False)), (b'question_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional expansion on intro', required=False)), (b'radio_intro', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Leave blank unless you are building a feedback form with extra radio-button prompts, as in /owning-a-home/help-us-improve/.', required=False)), (b'radio_text', wagtail.wagtailcore.blocks.CharBlock(default=b'This information helps us understand your question better.', required=False)), (b'radio_question_1', wagtail.wagtailcore.blocks.CharBlock(default=b'How soon do you expect to buy a home?', required=False)), (b'radio_question_2', wagtail.wagtailcore.blocks.CharBlock(default=b'Do you currently own a home?', required=False)), (b'button_text', wagtail.wagtailcore.blocks.CharBlock(default=b'Submit')), (b'contact_advisory', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Use only for feedback forms that ask for a contact email', required=False))]))]),
        ),
    ]
