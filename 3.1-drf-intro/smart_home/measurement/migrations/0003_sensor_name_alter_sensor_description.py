# Generated by Django 4.2.3 on 2023-10-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_measurement_sensor_delete_weapon_measurement_sensor'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='name',
            field=models.CharField(default='new_sensor', max_length=20),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
