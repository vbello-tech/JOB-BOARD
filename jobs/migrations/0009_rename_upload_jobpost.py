# Generated by Django 4.2.2 on 2023-07-14 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_bookmark'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Upload',
            new_name='Jobpost',
        ),
    ]