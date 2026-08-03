import re

from django.core.exceptions import ValidationError


def validate_strong_password(password):

    if not re.search(r"[A-Z]", password):
        raise ValidationError(
            "Password must contain at least one uppercase letter."
        )


    if not re.search(r"[a-z]", password):
        raise ValidationError(
            "Password must contain at least one lowercase letter."
        )


    if not re.search(r"[0-9]", password):
        raise ValidationError(
            "Password must contain at least one number."
        )


    if not re.search(r"[@$!%*?&#]", password):
        raise ValidationError(
            "Password must contain at least one special character."
        )