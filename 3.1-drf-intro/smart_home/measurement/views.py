from rest_framework import status
from django.db import connection
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorCreateSerializer, SensorDetailSerializer


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


class MeasurementView(CreateAPIView):
    serializer_class = MeasurementSerializer

    def create(self, request, *args, **kwargs):
        sensor_name = request.data.get('sensor')
        try:
            sensor = Sensor.objects.get(name=sensor_name)
        except Sensor.DoesNotExist:
            return Response({'error': 'Sensor not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(sensor=sensor)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SensorDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
