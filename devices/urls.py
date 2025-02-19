from django.urls import path
from .views import *

urlpatterns = [
    path('areas/',AreaControlListCreateView.as_view(),name='Areas-list'),
    path('devices/',DeviceListCreateView.as_view(),name='Devices-list')
]