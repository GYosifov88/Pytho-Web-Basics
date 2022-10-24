from django.core.exceptions import ValidationError


def genre_validator(id):
    if id == 0:
        raise ValidationError('Please select genre')
