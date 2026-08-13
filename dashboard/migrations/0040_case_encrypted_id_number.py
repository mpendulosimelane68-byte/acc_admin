from django.db import migrations, models
import os
from cryptography.fernet import Fernet


def encrypt_existing_id_numbers(apps, schema_editor):
    Case = apps.get_model("dashboard", "Case")

    key = os.environ.get("FIELD_ENCRYPTION_KEY")

    if not key:
        raise RuntimeError(
            "FIELD_ENCRYPTION_KEY environment variable is not set."
        )

    fernet = Fernet(key.encode())

    for case in Case.objects.exclude(id_number__isnull=True).exclude(id_number=""):
        case.encrypted_id_number = fernet.encrypt(
            case.id_number.encode()
        ).decode()

        case.save(
            update_fields=["encrypted_id_number"]
        )


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0039_case_account"),
    ]

    operations = [
        migrations.AddField(
            model_name="case",
            name="encrypted_id_number",
            field=models.TextField(
                blank=True,
                null=True,
            ),
        ),

        migrations.RunPython(
            encrypt_existing_id_numbers,
            migrations.RunPython.noop,
        ),
    ]