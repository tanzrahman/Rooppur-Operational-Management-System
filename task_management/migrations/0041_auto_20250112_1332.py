# Generated by Django 3.2.16 on 2025-01-12 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_management', '0040_documentreviewcomments_secondtiercommitteefeedback_secondtierdocumentreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentreviewcomments',
            name='second_tier_committee_feedback',
        ),
        migrations.AddField(
            model_name='documentreviewcomments',
            name='second_tier_committee_review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='task_management.secondtierdocumentreview'),
        ),
    ]
