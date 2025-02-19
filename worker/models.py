from django.db import models
from django.contrib.auth.models import User
from devices.models import AreaControl


class Rol(models.Model):
    rolType = models.CharField(choices=[('Administrator','Administrator'),('Controller','Controller'),('Operator','Operator')], max_length=20)
    description = models.CharField(max_length=50)
    allowedAreas = models.ManyToManyField(AreaControl)
    
    def __str__(self):
       return f"{self.rolType} - {self.description}"     
    
class Profile(User):
    rol = models.ForeignKey('Rol', on_delete=models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        verbose_name='Profile' 
        
    
    
    