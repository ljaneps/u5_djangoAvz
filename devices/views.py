from rest_framework import generics
from .models import *
from .serializers import *

class AreaControlListCreateView(generics.ListCreateAPIView):
    queryset = AreaControl.objects.all()
    serializer_class = AreaSerializer
    
class AreaControlUpdateCreateView(generics.RetrieveUpdateAPIView):
    queryset = AreaControl.objects.all()
    serializer_class = AreaSerializer
    lookup_field = 'id'

class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    
class DeviceDestroyCreateView(generics.DestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = 'id'
