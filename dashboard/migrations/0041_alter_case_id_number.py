import dashboard.encrypted_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0040_case_encrypted_id_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="case",
            name="id_number",
            field=dashboard.encrypted_fields.EncryptedCharField(
                blank=True,
                null=True,
            ),
        ),
    ]