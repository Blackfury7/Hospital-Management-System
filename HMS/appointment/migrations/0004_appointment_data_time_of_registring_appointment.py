# Generated by Django 2.2 on 2020-06-22 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_auto_20200623_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment_data',
            name='time_of_registring_appointment',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
