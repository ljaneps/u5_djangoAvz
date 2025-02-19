from rest_framework import generics
from .models import *
from .serializers import *

class RolListCreateView(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    
class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Profile.objects.all()
        serializer_class = ProfileSerializer