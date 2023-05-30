# Generated by Django 4.2.1 on 2023-05-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carblog', '0005_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Volvo', max_length=255),
        ),
    ]