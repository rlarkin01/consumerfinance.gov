# Generated by Django 3.2.12 on 2022-03-14 23:57

import django.db.models.deletion
from django.db import migrations, models

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks

import v1.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('v1', '0199_2022_squash'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormExplainerPage',
            fields=[
                ('cfgovpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='v1.cfgovpage')),
                ('header', wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(help_text='For complete guidelines on creating heroes, visit our <a href="https://cfpb.github.io/design-system/components/heroes">Design System</a>. Character counts (including spaces) at largest breakpoint:<ul class="help">    <li>&bull; 41 characters max (one-line heading)</li>    <li>&bull; 82 characters max (two-line heading)</li></ul>', required=False)), ('body', wagtail.blocks.RichTextBlock(help_text='Character counts (including spaces) at largest breakpoint:<ul class="help">    <li>&bull; 165-186 characters (after a one-line heading)</li>    <li>&bull; 108-124 characters (after a two-line heading)</li></ul>', label='Sub-heading', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='When saving illustrations, use a transparent background. <a href="https://cfpb.github.io/design-system/components/heroes#style">See image dimension guidelines.</a>', label='Large image', required=False)), ('small_image', wagtail.images.blocks.ImageChooserBlock(help_text='<b>Optional.</b> Provides an alternate image for small displays when using a photo or bleeding hero. Not required for the standard illustration. <a href="https://cfpb.github.io/design-system/components/heroes#style">See image dimension guidelines.</a>', required=False)), ('background_color', wagtail.blocks.CharBlock(help_text='Specify a hex value (including the # sign) from our <a href="https://cfpb.github.io/design-system/foundation/color">official color palette</a>.', required=False)), ('is_white_text', wagtail.blocks.BooleanBlock(help_text='<b>Optional.</b> Turns the hero text white. Useful if using a dark background color or background image.', label='White text', required=False)), ('is_overlay', wagtail.blocks.BooleanBlock(help_text='<b>Optional.</b> Uses the large image as a background under the entire hero, creating the "Photo" style of hero (see <a href="https://cfpb.github.io/design-system/components/heroes">Design System</a> for details). When using this option, make sure to specify a background color (above) for the left/right margins that appear when screens are wider than 1200px and for the text section when the photo and text stack at mobile sizes.', label='Photo', required=False)), ('is_bleeding', wagtail.blocks.BooleanBlock(help_text='<b>Optional.</b> Select if you want the illustration to bleed vertically off the top and bottom of the hero space.', label='Bleed', required=False))])), ('text_introduction', wagtail.blocks.StructBlock([('eyebrow', wagtail.blocks.CharBlock(help_text='Optional: Adds an H5 eyebrow above H1 heading text. Only use in conjunction with heading.', label='Pre-heading', required=False)), ('heading', wagtail.blocks.CharBlock(required=False)), ('intro', wagtail.blocks.RichTextBlock(required=False)), ('body', wagtail.blocks.RichTextBlock(required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False))]), required=False)), ('has_rule', wagtail.blocks.BooleanBlock(help_text='Check this to add a horizontal rule line to bottom of text introduction.', label='Has bottom rule', required=False))]))], blank=True)),
                ('content', wagtail.fields.StreamField([('explainer', wagtail.blocks.StructBlock([('pages', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(icon='image', required=True)), ('categories', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Optional. Leave blank if there is only one type of note for this image.', label='Category title', required=False)), ('notes', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('coordinates', wagtail.blocks.StructBlock([('left', wagtail.blocks.FloatBlock(max_value=100, min_value=0, required=True)), ('top', wagtail.blocks.FloatBlock(max_value=100, min_value=0, required=True)), ('width', wagtail.blocks.FloatBlock(max_value=100, min_value=0, required=True)), ('height', wagtail.blocks.FloatBlock(max_value=100, min_value=0, required=True))], form_classname='coordinates', help_text='Enter percentage values to define the area that will be highlighted on the image for this note.', label='Note image map coordinates')), ('heading', wagtail.blocks.CharBlock(label='Note heading', required=True)), ('body', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'document-link'], label='Note text', required=True))], form_classname='explainer_notes', required=False), default=[]))], required=False)))], required=False)))])), ('well', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(label='Well', required=False))])), ('info_unit_group', wagtail.blocks.StructBlock([('format', wagtail.blocks.ChoiceBlock(choices=[('50-50', '50/50'), ('33-33-33', '33/33/33'), ('25-75', '25/75')], help_text='Choose the number and width of info unit columns.', label='Format')), ('heading', wagtail.blocks.StructBlock([('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], required=False)), ('intro', wagtail.blocks.RichTextBlock(required=False)), ('link_image_and_heading', wagtail.blocks.BooleanBlock(default=True, help_text="Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", required=False)), ('has_top_rule_line', wagtail.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of info unit group.', required=False)), ('lines_between_items', wagtail.blocks.BooleanBlock(default=False, help_text='Check this to show horizontal rule lines between info units.', label='Show rule lines between items', required=False)), ('info_units', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.blocks.StructBlock([('upload', wagtail.images.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.blocks.CharBlock(help_text="No character limit, but be as succinct as possible. If the image is decorative (i.e., a screenreader wouldn't have anything useful to say about it), leave this field blank.", required=False))])), ('heading', wagtail.blocks.StructBlock([('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/design-system/foundation/iconography">See full list of icons</a>', required=False))], default={'level': 'h3'}, required=False)), ('body', wagtail.blocks.RichTextBlock(blank=True, required=False)), ('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=False)), ('aria_label', wagtail.blocks.CharBlock(help_text='Add an ARIA label if the link text does not describe the destination of the link (e.g. has ambiguous text like "Learn more" that is not descriptive on its own).', required=False)), ('url', wagtail.blocks.CharBlock(default='/', required=False))]), required=False))]), default=[])), ('sharing', wagtail.blocks.StructBlock([('shareable', wagtail.blocks.BooleanBlock(help_text='If checked, share links will be included below the items.', label='Include sharing links?', required=False)), ('share_blurb', wagtail.blocks.CharBlock(help_text='Sets the tweet text, email subject line, and LinkedIn post text.', required=False))]))])), ('feedback', wagtail.blocks.StructBlock([('was_it_helpful_text', wagtail.blocks.CharBlock(default='Was this page helpful to you?', help_text='Use this field only for feedback forms that use "Was this helpful?" radio buttons.', required=False)), ('intro_text', wagtail.blocks.CharBlock(help_text='Optional feedback intro', required=False)), ('question_text', wagtail.blocks.CharBlock(help_text='Optional expansion on intro', required=False)), ('radio_intro', wagtail.blocks.CharBlock(help_text='Leave blank unless you are building a feedback form with extra radio-button prompts, as in /owning-a-home/help-us-improve/.', required=False)), ('radio_text', wagtail.blocks.CharBlock(default='This information helps us understand your question better.', required=False)), ('radio_question_1', wagtail.blocks.CharBlock(default='How soon do you expect to buy a home?', required=False)), ('radio_question_2', wagtail.blocks.CharBlock(default='Do you currently own a home?', required=False)), ('button_text', wagtail.blocks.CharBlock(default='Submit')), ('contact_advisory', wagtail.blocks.RichTextBlock(help_text='Use only for feedback forms that ask for a contact email', required=False))]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('v1.cfgovpage',),
        ),
    ]
