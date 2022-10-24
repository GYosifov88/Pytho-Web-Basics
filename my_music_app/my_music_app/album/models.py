from django.core.validators import MinValueValidator
from django.db import models


class Album(models.Model):

    album_name = models.CharField(
        unique=True,
        max_length=30,
        null=False,
        blank=False,
    )

    artist = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )

    genre = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(0.0)]
    )
