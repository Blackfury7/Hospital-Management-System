# Generated by Django 2.2 on 2020-06-24 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0008_auto_20200625_0109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment_data',
            old_name='receptionist_approval',
            new_name='receptionist_response',
        ),
    ]