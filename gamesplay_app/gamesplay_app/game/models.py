from django.db import models

from gamesplay_app.game.validators import validate_rating_min, validate_max_level


class Game(models.Model):
    CATEGORIES = (
        (1, "Action"),
        (2, "Adventure"),
        (3, "Puzzle"),
        (4, "Strategy"),
        (5, "Sports"),
        (6, "Board/Card Game"),
        (7, "Other"),
    )
    MAX_TITLE_LENGTH = 30
    MAX_CATEGORY_LENGTH = 15

    title = models.CharField(blank=False, max_length=MAX_TITLE_LENGTH, unique=True)
    category = models.CharField(max_length=MAX_CATEGORY_LENGTH, choices=CATEGORIES)
    rating = models.FloatField(max_length=5.0, validators=(validate_rating_min,), blank=False)
    max_level = models.IntegerField(validators=(validate_max_level,), null=True, blank=True)
    image = models.URLField(blank=False)
    summary = models.TextField(blank=True, null=True)
