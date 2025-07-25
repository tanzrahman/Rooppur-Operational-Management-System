# Generated by Django 3.2.16 on 2024-06-04 04:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task_management', '0019_auto_20240602_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskfeedback',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 10, 6, 13, 204544), null=True),
        ),
        migrations.CreateModel(
            name='ExternalParticipants',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('participants', models.TextField(blank=True, max_length=3072, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('lecture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='task_management.lecture')),
            ],
        ),
    ]
