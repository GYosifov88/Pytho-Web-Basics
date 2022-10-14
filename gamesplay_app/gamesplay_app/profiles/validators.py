from django.core.exceptions import ValidationError


def validate_min_age(num):
    if num < 12:
        raise ValidationError("Minimal Age is 12")

