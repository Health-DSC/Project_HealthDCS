from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from .choices import sexos,estado_civil,tipo_sangre

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    sexo = models.CharField(max_length=12,choices=sexos,verbose_name='Sexo')
    estado_civil = models.CharField(max_length=20, choices=estado_civil,verbose_name='Ingrese su estado civil')
    def __str__(self):
        return "%s"% self.id

class Medico(models.Model):
    persona = models.OneToOneField(Persona,on_delete=models.CASCADE,primary_key=True)
    habilitado = models.BooleanField(default=1)

class Paciente(models.Model):
    persona = models.OneToOneField(Persona,on_delete=models.CASCADE,primary_key=True)
    id_seguro = models.IntegerField(default=0)
    tipo_sangre = models.CharField(max_length=3,choices=tipo_sangre,default='O')
