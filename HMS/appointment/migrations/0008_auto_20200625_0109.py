# Generated by Django 2.2 on 2020-06-24 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0007_appointment_data_after_disease'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment_data',
            old_name='time_of_registring_appointment',
            new_name='time_of_registering_appointment',
        ),
    ]