from rest_framework import serializers
from .models import *

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id','name','type','description',]


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaControl
        fields = ['id','areaControl','description',]