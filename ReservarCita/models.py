from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from .choices import sexos,estado_civil,tipo_sangre,area
import datetime

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    sexo = models.CharField(max_length=12,choices=sexos,verbose_name='Sexo')
    estado_civil = models.CharField(max_length=20, choices=estado_civil,verbose_name='Ingrese su estado civil')
    
    #Renombrar el objeto
    def __str__(self):
        nombre_completo =self.nombres + " " + self.apellidos
        return nombre_completo

class Medico(models.Model):
    persona = models.OneToOneField(Persona,on_delete=models.CASCADE,primary_key=True)
    habilitado = models.BooleanField(default=1)

class Paciente(models.Model):
    persona = models.OneToOneField(Persona,on_delete=models.CASCADE,primary_key=True)
    id_seguro = models.IntegerField(default=0)
    tipo_sangre = models.CharField(max_length=3,choices=tipo_sangre,default='O')


class Tecnologo(models.Model):
    persona = models.OneToOneField(Persona,on_delete=models.CASCADE,primary_key=True)
    area = models.CharField(max_length=12,choices=area,default='Radiologia')

class Cita(models.Model):
    fecha = models.DateField(default=datetime.date.today)
    hora = models.TimeField(default=datetime.time)
    confirmacion = models.BooleanField(default=1)
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico,on_delete=models.CASCADE)
    tecnologo = models.ForeignKey(Tecnologo,on_delete=models.CASCADE)

    def __str__(self):
        nombre_paciente =self.paciente
        nombre_medico =self.medico
        nombre_tecnologo =self.tecnologo
        return nombre_paciente,nombre_medico,nombre_tecnologo 
