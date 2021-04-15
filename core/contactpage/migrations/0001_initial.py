# Generated by Django 3.1.5 on 2021-04-15 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=50, verbose_name='Əlaqə nömrəsi')),
                ('address', models.CharField(max_length=300, verbose_name='Ünvan')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, verbose_name='Istifadəçi adı')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=50, verbose_name='İstifadəçinin əlaqə nömrəsi')),
                ('message', models.TextField(verbose_name='İstifadəçi mesajı')),
            ],
            options={
                'verbose_name_plural': 'Əlaqə saxlamaq istəyən istifadəçilər',
            },
        ),
    ]
