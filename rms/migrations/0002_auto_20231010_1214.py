# Generated by Django 3.2.22 on 2023-10-10 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hr_registration',
            old_name='department',
            new_name='hr_name',
        ),
        migrations.RemoveField(
            model_name='hr_registration',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='hr_registration',
            name='last_name',
        ),
    ]
