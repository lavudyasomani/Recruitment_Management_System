# Generated by Django 3.2.22 on 2023-10-11 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0004_rename_hr_interview_declaration_form_hr_interview_declaration'),
    ]

    operations = [
        migrations.AddField(
            model_name='hr_interview_declaration',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
