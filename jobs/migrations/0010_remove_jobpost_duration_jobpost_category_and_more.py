# Generated by Django 4.2.2 on 2023-07-14 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_rename_upload_jobpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='Duration',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='Category',
            field=models.TextField(choices=[('FULL TIME', 'FULL TIME'), ('INTERNSHIP', 'INTERNSHIP'), ('CONTRACT', 'CONTRACT')], null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='Description',
            field=models.CharField(max_length=200),
        ),
    ]
