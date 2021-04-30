# Generated by Django 3.1.5 on 2021-04-19 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutpage', '0002_about_about_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_context_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='about_context_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='about_context_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='about_title_az',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='about_title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='about_title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
    ]