# Generated by Django 5.0.4 on 2025-06-29 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manpower', '0009_alter_approvalsignature_remarks_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvalsignature',
            name='remarks_1',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
