from django.db import models


class AreaControl(models.Model):
    areaControl = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.areaControl 

class Device(models.Model):
    type = models.CharField(choices=[('Panel', 'Panel'),('Camera','Camera'),('sos','Poste SOS')], max_length=20)
    area = models.ForeignKey('AreaControl', on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50) 
    
    