from django.urls import path
from django.views.decorators.http import require_http_methods
from measurement.views import SensorListView, MeasurementView, SensorCreateView, SensorUpdateView, SensorDetailView

urlpatterns = [
    path('sensors/', SensorListView.as_view(), name='sensors-list'),
    path('create_sensor/', SensorCreateView.as_view(), name='sensor-create'),
    path('sensors/<pk>/', SensorUpdateView.as_view(), name='sensor-update'),
    path('measurements/', MeasurementView.as_view(), name='measurement-add'),
    path('sensor/<pk>/', SensorDetailView.as_view(), name='sensor-detail'),
]
