from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=False,
    )

    last_name = models.CharField(
        max_length=20,
        blank=False,
    )

    age = models.IntegerField()

    image_url = models.URLField()


class Note(models.Model):
    title = models.CharField(
        max_length=30,
        blank=False,
    )

    image_url = models.URLField()

    content = models.TextField()