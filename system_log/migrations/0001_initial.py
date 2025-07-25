# Generated by Django 5.0.6 on 2024-05-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentApprovalLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=256, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('ip', models.CharField(blank=True, max_length=256, null=True)),
                ('doc_id', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'document_approval_log',
            },
        ),
        migrations.CreateModel(
            name='DocumentLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=256, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('ip', models.CharField(blank=True, max_length=256, null=True)),
                ('doc_id', models.CharField(blank=True, max_length=256, null=True)),
                ('access_details', models.TextField(blank=True, max_length=1024, null=True)),
            ],
            options={
                'db_table': 'document_log',
            },
        ),
        migrations.CreateModel(
            name='FailedLoginLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=256, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('ip', models.CharField(blank=True, max_length=256, null=True)),
                ('login_attempt_count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'failed_login_log',
            },
        ),
        migrations.CreateModel(
            name='FileLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=256, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('ip', models.CharField(blank=True, max_length=256, null=True)),
                ('file_hash', models.CharField(blank=True, max_length=256, null=True)),
                ('access_type', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'file_log',
            },
        ),
        migrations.CreateModel(
            name='UserDeactivateLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=256, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('ip', models.CharField(blank=True, max_length=256, null=True)),
                ('deactivation_details', models.TextField(blank=True, max_length=1024, null=True)),
            ],
            options={
                'db_table': 'user_deactivate_log',
            },
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=256, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('ip', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'user_log',
            },
        ),
    ]
