# Generated by Django 5.0.4 on 2025-06-29 10:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_log', '0055_alter_documentlog_time_alter_failedloginlog_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentlog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 29, 16, 49, 40, 480152), null=True),
        ),
        migrations.AlterField(
            model_name='failedloginlog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 29, 16, 49, 40, 480152), null=True),
        ),
        migrations.AlterField(
            model_name='filelog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 29, 16, 49, 40, 480152), null=True),
        ),
        migrations.AlterField(
            model_name='mailandsmslog',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 29, 16, 49, 40, 488186), null=True),
        ),
        migrations.AlterField(
            model_name='userlog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 29, 16, 49, 40, 480152), null=True),
        ),
    ]
