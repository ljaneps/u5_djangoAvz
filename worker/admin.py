from django.contrib import admin
from .models import *

@admin.register(Rol) 
class RolAdmin(admin.ModelAdmin):
    list_display = ('rolType','description',)
    
@admin.register(Profile)
class profileAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','rol')