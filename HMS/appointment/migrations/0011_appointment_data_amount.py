# Generated by Django 2.2 on 2020-06-25 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0010_auto_20200625_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment_data',
            name='amount',
            field=models.CharField(default='500', max_length=200),
        ),
    ]