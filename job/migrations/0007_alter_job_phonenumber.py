# Generated by Django 4.2.5 on 2023-10-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_remove_apply_job_counter_job_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='phoneNumber',
            field=models.CharField(max_length=12),
        ),
    ]