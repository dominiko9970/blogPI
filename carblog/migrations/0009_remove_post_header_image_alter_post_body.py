# Generated by Django 4.2.1 on 2023-05-22 18:36

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carblog', '0008_post_header_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='header_image',
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]