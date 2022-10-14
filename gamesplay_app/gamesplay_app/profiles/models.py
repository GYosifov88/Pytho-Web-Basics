from django.core.validators import MinValueValidator
from django.db import models

from gamesplay_app.profiles.validators import validate_min_age


class Profile(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_PASSWORD_LENGTH = 30

    email = models.EmailField(blank=False)
    age = models.IntegerField(blank=False, validators=(validate_min_age,),)
    password = models.CharField(blank=False, max_length=MAX_PASSWORD_LENGTH,)
    first_name = models.CharField(max_length=MAX_NAME_LENGTH, null=True)
    last_name = models.CharField(max_length=MAX_NAME_LENGTH, null=True)
    profile_picture = models.URLField(null=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'



