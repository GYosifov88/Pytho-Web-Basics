# Generated by Django 4.1.2 on 2022-10-19 07:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30, unique=True)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[(8, 'Other'), (4, 'Rock Music'), (2, 'Jazz Music'), (6, 'Dance Music'), (3, 'R&B Music'), (1, 'Pop Music'), (5, 'Country Music'), (7, 'Hip Hop Music')], max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
    ]
