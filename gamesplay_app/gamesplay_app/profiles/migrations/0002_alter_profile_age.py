# Generated by Django 4.1.2 on 2022-10-14 08:07

from django.db import migrations, models
import gamesplay_app.profiles.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(validators=[gamesplay_app.profiles.validators.validate_min_age]),
        ),
    ]