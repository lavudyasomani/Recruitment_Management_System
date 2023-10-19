# Generated by Django 3.2.22 on 2023-10-12 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0005_hr_interview_declaration_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hr_registration',
            old_name='employee_id',
            new_name='hr_employ_id',
        ),
        migrations.AddField(
            model_name='hr_interview_declaration',
            name='hr_employ_id',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
