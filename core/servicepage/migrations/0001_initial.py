# Generated by Django 3.1.5 on 2021-04-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('service_description', models.CharField(max_length=200)),
                ('service_image', models.ImageField(upload_to='service/')),
                ('context', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
