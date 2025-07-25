# Generated by Django 3.2.16 on 2024-05-24 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_management', '0010_auto_20240523_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributorfeedback',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 24, 9, 53, 50, 579243)),
        ),
        migrations.AlterField(
            model_name='executorfeedback',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 24, 9, 53, 50, 577590)),
        ),
        migrations.AlterField(
            model_name='questionsanswers',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 24, 9, 53, 50, 575687)),
        ),
        migrations.AlterField(
            model_name='supervisorfeedback',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 24, 9, 53, 50, 578437)),
        ),
        migrations.AlterField(
            model_name='taskfeedback',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 24, 9, 53, 50, 580076)),
        ),
    ]
