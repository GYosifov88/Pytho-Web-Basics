from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        blank=True,
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
    )
    image_url = models.URLField(
        blank=True,
    )
