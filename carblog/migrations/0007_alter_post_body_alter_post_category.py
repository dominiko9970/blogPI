# Generated by Django 4.2.1 on 2023-05-22 08:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carblog', '0006_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='volvo', max_length=255),
        ),
    ]
