# Generated by Django 2.2 on 2020-06-22 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20200623_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment_data',
            name='date',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='appointment_data',
            name='time',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
