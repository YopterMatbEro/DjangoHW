from django.db import models
from datetime import datetime as dt


class Sensor(models.Model):
    name = models.CharField(max_length=20, default='new_sensor')
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
