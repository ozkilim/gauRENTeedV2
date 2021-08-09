from django.core.exceptions import ValidationError


def validate_no_gmail_siblings(value):
    if '+' in value and value.endswith('gmail.com'):
        raise ValidationError(
            "Please use your plain Gmail address"
        )
