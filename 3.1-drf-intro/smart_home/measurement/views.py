from rest_framework import status
from django.db import connection
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorCreateSerializer


class SensorListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def delete_unused_sensors(self):
        Sensor.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE measurement_sensor_id_seq RESTART WITH 1")

    def delete(self):
        self.delete_unused_sensors()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SensorCreateView(CreateAPIView):
    serializer_class = SensorCreateSerializer


class SensorUpdateView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementView(RetrieveAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
