# Generated by Django 3.2.16 on 2024-05-14 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manpower', '0002_ipwhitelist_denied'),
        ('task_management', '0007_task_division'),
    ]

    operations = [
        migrations.AddField(
            model_name='milestone',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manpower.division'),
        ),
    ]
