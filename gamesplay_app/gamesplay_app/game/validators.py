from django.core.exceptions import ValidationError


def validate_rating_min(num):
    if num < 0.1:
        raise ValidationError("Minimal Rating can't be below 0.1")


def validate_max_level(num):
    if num < 1:
        raise ValidationError("Max Level can't be below 1")
