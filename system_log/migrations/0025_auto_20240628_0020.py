# Generated by Django 3.2.16 on 2024-06-27 18:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_log', '0024_auto_20240627_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentlog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 28, 0, 20, 11, 840415), null=True),
        ),
        migrations.AlterField(
            model_name='failedloginlog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 28, 0, 20, 11, 840683), null=True),
        ),
        migrations.AlterField(
            model_name='filelog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 28, 0, 20, 11, 839771), null=True),
        ),
        migrations.AlterField(
            model_name='mailandsmslog',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 28, 0, 20, 11, 849921), null=True),
        ),
        migrations.AlterField(
            model_name='userlog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 28, 0, 20, 11, 839520), null=True),
        ),
    ]
