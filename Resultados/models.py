from django.db import models
from ReservarCita.models import Cita,Tecnologo

import datetime

# Create your models here.

class Resonancia(models.Model):
    title = models.CharField(max_length=100,default='') 
    fecha = models.DateField(default=datetime.date.today)
    descripcion = models.CharField(max_length=100,default='')   
    tecnologo = models.ForeignKey(Tecnologo,on_delete=models.CASCADE,null=True,blank=True)
    img = models.ImageField(upload_to = "Resultados/images",null = True, blank=True)

class Diagnostico(models.Model):
    resonancia = models.ForeignKey(Resonancia,on_delete=models.CASCADE,null=True,blank=True)
    descripcion = descripcion = models.CharField(max_length=200,default='')

class Tratamiento(models.Model):
    Diagnostico = models.ForeignKey(Diagnostico,on_delete=models.CASCADE,null=True,blank=True)
    descripcion = descripcion = models.CharField(max_length=200,default='')

class Resultado(models.Model):
    cita = models.ForeignKey(Cita,on_delete=models.CASCADE,null=True,blank=True)
    resonancia = models.ForeignKey(Resonancia,on_delete=models.CASCADE,null=True,blank=True)

