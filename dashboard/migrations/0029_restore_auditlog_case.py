from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0005_alter_report_age_group'),
        ('dashboard', '0028_notification_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditlog',
            name='case',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='cases.case',
            ),
        ),
    ]