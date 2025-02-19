from django.contrib import admin
from .models import *

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name','type','description',)

@admin.register(AreaControl)
class AreaControlAdmin(admin.ModelAdmin):
    list_display = ('areaControl','description',)