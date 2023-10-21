# Generated by Django 4.2.5 on 2023-10-18 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_apply_job_counter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply_job',
            name='counter',
        ),
        migrations.AddField(
            model_name='job',
            name='counter',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]