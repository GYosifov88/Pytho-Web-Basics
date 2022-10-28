# Generated by Django 4.1.2 on 2022-10-28 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesplay_web_app', '0002_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='category',
            field=models.CharField(choices=[('ACTION', 'Action'), ('ADVENTURE', 'Adventure'), ('PUZZLE', 'Puzzle'), ('STRATEGY', 'Strategy'), ('SPORTS', 'Sports'), ('BOARD_CARD', 'Board/Card Game'), ('OTHER', 'Other')], max_length=15),
        ),
    ]
