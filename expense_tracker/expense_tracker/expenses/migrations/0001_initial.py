# Generated by Django 4.1.2 on 2022-10-07 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
