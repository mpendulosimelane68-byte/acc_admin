import os

from cryptography.fernet import Fernet
from django.db import models


class EncryptedCharField(models.TextField):
    description = "Encrypted text field"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        key = os.environ.get("FIELD_ENCRYPTION_KEY")

        if not key:
            raise ValueError(
                "FIELD_ENCRYPTION_KEY environment variable is not set."
            )

        self.fernet = Fernet(key.encode())

    def get_prep_value(self, value):
        if value is None:
            return None

        if value == "":
            return ""

        return self.fernet.encrypt(
            str(value).encode()
        ).decode()

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None

        if value == "":
            return ""

        return self.fernet.decrypt(
            value.encode()
        ).decode()

    def to_python(self, value):
        if value is None or value == "":
            return value

        # Already decrypted
        try:
            if not isinstance(value, str):
                return value

            return self.fernet.decrypt(
                value.encode()
            ).decode()
        except Exception:
            return value