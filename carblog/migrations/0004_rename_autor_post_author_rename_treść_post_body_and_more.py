# Generated by Django 4.2.1 on 2023-05-20 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carblog', '0003_rename_author_post_autor_rename_title_tag_post_tag_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='treść',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tytuł',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='title_tag',
        ),
    ]
