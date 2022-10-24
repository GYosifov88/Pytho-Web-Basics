from django.core.validators import MinLengthValidator
from django.db import models


class Profile(models.Model):
    MAX_LEN_TEXT = 15
    username = models.CharField(
        max_length=MAX_LEN_TEXT,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2)],
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=False,
    )
