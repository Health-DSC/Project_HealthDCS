from django.db import models
from ReservarCita.models import Cita,Tecnologo

import datetime

# Create your models here.
class Recurso(models.Model):
    fecha = models.DateField(default=datetime.date.today)
    descripcion = models.CharField(max_length=100,default='')
    ruta = models.URLField(default='')

class Resonancia(models.Model):
    recurso = models.ForeignKey(Recurso,on_delete=models.CASCADE,null=True,blank=True)
    tecnologo = models.ForeignKey(Tecnologo,on_delete=models.CASCADE,null=True,blank=True)

class Imagen(models.Model):
    recurso = models.ForeignKey(Recurso,on_delete=models.CASCADE,null=True,blank=True)
    probabilidad = models.FloatField(default=0.0)
    precision = models.FloatField(default=0.0)

class Diagnostico(models.Model):
    imagen = models.ForeignKey(Imagen,on_delete=models.CASCADE,null=True,blank=True)
    descripcion = descripcion = models.CharField(max_length=200,default='')

class Tratamiento(models.Model):
    Diagnostico = models.ForeignKey(Diagnostico,on_delete=models.CASCADE,null=True,blank=True)
    descripcion = descripcion = models.CharField(max_length=200,default='')

class Resultado(models.Model):
    cita = models.ForeignKey(Cita,on_delete=models.CASCADE,null=True,blank=True)
    resonancia = models.ForeignKey(Resonancia,on_delete=models.CASCADE,null=True,blank=True)

