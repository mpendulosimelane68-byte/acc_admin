import os

from cryptography.fernet import Fernet
from django.core.management.base import BaseCommand

from dashboard.models import Case


class Command(BaseCommand):
    help = "Encrypt existing plaintext ID numbers"

    def handle(self, *args, **options):
        key = os.environ.get("FIELD_ENCRYPTION_KEY")

        if not key:
            raise RuntimeError(
                "FIELD_ENCRYPTION_KEY environment variable is not set."
            )

        fernet = Fernet(key.encode())

        cases = Case.objects.exclude(
            id_number__isnull=True
        ).exclude(
            id_number=""
        )

        encrypted_count = 0
        skipped_count = 0

        for case in cases:
            if case.encrypted_id_number:
                skipped_count += 1
                continue

            case.encrypted_id_number = fernet.encrypt(
                case.id_number.encode()
            ).decode()

            case.save(
                update_fields=["encrypted_id_number"]
            )

            encrypted_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Encrypted {encrypted_count} ID number(s)."
            )
        )

        self.stdout.write(
            f"Skipped {skipped_count} already-encrypted record(s)."
        )