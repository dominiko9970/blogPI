# Generated by Django 4.2.1 on 2023-05-20 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='cars', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
