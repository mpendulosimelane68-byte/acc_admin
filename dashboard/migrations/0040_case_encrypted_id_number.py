from django.db import migrations, models


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
    ]