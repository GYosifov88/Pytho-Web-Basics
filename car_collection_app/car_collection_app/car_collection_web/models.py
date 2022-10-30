from enum import Enum

from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from car_collection_app.car_collection_web.validators import min_username_length_validator, car_year_validator


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 10
    MAX_PASSWORD_LENGTH = 30
    MAX_FIRST_NAME_LENGTH = 30
    MAX_LAST_NAME_LENGTH = 30

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=[min_username_length_validator, ],
        blank=False,
        null=False,
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        validators=[MinValueValidator(18), ],
        blank=False,
        null=False,
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=True,
        null=True,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        blank=True,
        null=True,
        verbose_name='Last Name',
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name='Profile Picture',
    )


class CarTypeChoices(Enum):
    SPORTS_CAR = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class Car(models.Model):
    MAX_CAR_TYPE_LENGTH = 10
    MAX_CAR_MODEL_LENGTH = 20

    type = models.CharField(
        max_length=MAX_CAR_TYPE_LENGTH,
        choices=CarTypeChoices.choices(),
        blank=False,
        null=False,
    )

    model = models.CharField(
        max_length=MAX_CAR_MODEL_LENGTH,
        validators=[MinLengthValidator(2), ],
        blank=False,
        null=False,
    )

    year = models.IntegerField(
        validators=[car_year_validator, ],
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        validators=[MinValueValidator(1), ],
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ('pk', )

