# Generated by Django 3.2.22 on 2023-10-14 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0006_auto_20231012_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Interview_Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rms.course')),
            ],
        ),
        migrations.AddField(
            model_name='hr_interview_declaration',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='rms.course'),
            preserve_default=False,
        ),
    ]
