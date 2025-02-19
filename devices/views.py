from rest_framework import generics
from .models import *
from .serializers import *

class AreaControlListCreateView(generics.ListCreateAPIView):
    queryset = AreaControl.objects.all()
    serializer_class = AreaSerializer
    
class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
