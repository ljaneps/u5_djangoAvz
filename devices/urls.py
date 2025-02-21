from django.urls import path
from .views import *

urlpatterns = [
    path('areas/',AreaControlListCreateView.as_view(),name='areas-list'),
    path('areas/<int:id>',AreaControlUpdateCreateView.as_view(),name='areas-update'),
    path('devices/',DeviceListCreateView.as_view(),name='devices-list'),
    path('devices/<int:id>',DeviceDestroyCreateView.as_view(),name='devices-delete')
]