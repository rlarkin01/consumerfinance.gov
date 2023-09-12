# Generated by Django 3.2.20 on 2023-09-12 18:37

from django.db import migrations

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0007_deprecate_iug_sharing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sublandingpage',
            name='sidebar_breakout',
            field=wagtail.fields.StreamField([('slug', wagtail.blocks.CharBlock(icon='title')), ('paragraph', wagtail.blocks.RichTextBlock(icon='edit')), ('breakout_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('is_round', wagtail.blocks.BooleanBlock(default=True, label='Round?', required=False)), ('icon', wagtail.blocks.CharBlock(help_text='Enter icon class name.')), ('heading', wagtail.blocks.CharBlock(label='Introduction Heading', required=False)), ('body', wagtail.blocks.TextBlock(label='Introduction Body', required=False))], heading='Breakout Image', icon='image')), ('job_listing_list', wagtail.blocks.StructBlock([('more_jobs_page', wagtail.blocks.PageChooserBlock(help_text='Link to full list of jobs'))]))], blank=True, use_json_field=True),
        ),
    ]
