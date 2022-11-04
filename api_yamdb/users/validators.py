from django.core.exceptions import ValidationError


def validate_username(value):
    if value == 'me':
        raise ValidationError(
            ('Ник не может быть <me>.'),
            params={'value': value},
        )