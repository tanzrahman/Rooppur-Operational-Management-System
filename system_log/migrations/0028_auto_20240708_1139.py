# Generated by Django 3.2.16 on 2024-07-08 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_log', '0027_auto_20240701_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentlog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 8, 11, 39, 38, 741058), null=True),
        ),
        migrations.AlterField(
            model_name='failedloginlog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 8, 11, 39, 38, 741310), null=True),
        ),
        migrations.AlterField(
            model_name='filelog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 8, 11, 39, 38, 740433), null=True),
        ),
        migrations.AlterField(
            model_name='mailandsmslog',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 8, 11, 39, 38, 752366), null=True),
        ),
        migrations.AlterField(
            model_name='userlog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 8, 11, 39, 38, 740193), null=True),
        ),
    ]
