from django.db import models


class Recipe(models.Model):
    title = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )

    image_url = models.URLField()

    description = models.TextField()

    ingredients = models.CharField(
        max_length=250,
        blank=False,
        null=False,
    )

    time = models.IntegerField(
        verbose_name='Time (Minutes)'
    )