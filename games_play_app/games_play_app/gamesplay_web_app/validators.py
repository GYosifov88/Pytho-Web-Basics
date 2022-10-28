from django.core.exceptions import ValidationError


def age_validator(value):
    if value < 12:
        raise ValidationError("Age cannot be under 12")