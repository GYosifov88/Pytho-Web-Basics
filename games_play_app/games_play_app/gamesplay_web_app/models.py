from enum import Enum

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from games_play_app.gamesplay_web_app.validators import age_validator


class Profile(models.Model):
    MAX_PASS_LENGTH = 30
    MAX_FIRST_NAME_LENGTH = 30
    MAX_LAST_NAME_LENGTH = 30

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        validators=[age_validator,],
        blank=False,
        null=False,
    )

    password = models.CharField(
        max_length=MAX_PASS_LENGTH,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=True,
        null=True,
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        blank=True,
        null=True,
        verbose_name='Last Name'
    )

    profile_pic = models.URLField(
        blank=True,
        null=True,
        verbose_name='Profile Picture'
    )


class CategoryChoices(Enum):
    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    PUZZLE = 'Puzzle'
    STRATEGY = 'Strategy'
    SPORTS = 'Sports'
    BOARD_CARD = 'Board/Card Game'
    OTHER = 'Other'

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class Game(models.Model):
    MAX_GAME_TITLE_LENGTH = 30
    MAX_GAME_CATEGORY_LENGTH = 15

    title = models.CharField(
        max_length=MAX_GAME_TITLE_LENGTH,
        unique=True,
        blank=False,
        null=False,
    )

    category = models.CharField(
        max_length=MAX_GAME_CATEGORY_LENGTH,
        blank=False,
        null=False,
        choices=CategoryChoices.choices(),
    )

    rating = models.FloatField(
        validators=[MinValueValidator(0.1), MaxValueValidator(5.0)],
        blank=False,
        null=False,
    )

    max_level = models.IntegerField(
        validators=[MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name='Max Level'
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image URL'
    )

    summary = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('pk', )
