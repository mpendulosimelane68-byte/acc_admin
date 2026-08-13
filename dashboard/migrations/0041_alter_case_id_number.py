import dashboard.encrypted_fields
from django.db import migrations


def copy_encrypted_ids(apps, schema_editor):
    Case = apps.get_model("dashboard", "Case")

    table = Case._meta.db_table
    quoted_table = schema_editor.quote_name(table)

    with schema_editor.connection.cursor() as cursor:
        cursor.execute(
            f"""
            UPDATE {quoted_table}
            SET id_number = encrypted_id_number
            WHERE encrypted_id_number IS NOT NULL
              AND encrypted_id_number != ''
            """
        )


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0040_case_encrypted_id_number"),
    ]

    operations = [
        migrations.RunPython(
            copy_encrypted_ids,
            migrations.RunPython.noop,
        ),

        migrations.AlterField(
            model_name="case",
            name="id_number",
            field=dashboard.encrypted_fields.EncryptedCharField(
                blank=True,
                max_length=30,
                null=True,
            ),
        ),
    ]