# Generated by Django 4.2.1 on 2023-05-22 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carblog', '0009_remove_post_header_image_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]