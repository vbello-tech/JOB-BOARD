# Generated by Django 4.2.2 on 2023-07-03 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_upload_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='Countdown',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='JobDuration',
        ),
        migrations.AddField(
            model_name='upload',
            name='Duration',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='Onsite',
            field=models.BooleanField(null=True),
        ),
    ]
