from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from .choices import sexos,estado_civil,tipo_sangre,area,especialidades
import datetime

# Create your models here.
class Turno(models.Model):
    id_turno =models.CharField(max_length=8,default='',primary_key=True, verbose_name='Código del turno')
    hora_inicio = models.TimeField(default=datetime.time,verbose_name='Hora de inicio')
    hora_fin = models.TimeField(default=datetime.time,verbose_name='Hora de termino')

class Horario(models.Model):
    turno = models.ForeignKey(Turno,on_delete=models.CASCADE)
    hora_inicio = models.TimeField(default=datetime.time,verbose_name='Hora de inicio')
    hora_fin = models.TimeField(default=datetime.time,verbose_name='Hora de termino')

class Persona(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    dni = models.IntegerField(default=73118828,verbose_name='DNI')
    sexo = models.CharField(max_length=12,choices=sexos,verbose_name='Sexo')
    fecha_nacimiento = models.DateField(default=datetime.date.today,verbose_name='Fecha de nacimiento')
    estado_civil = models.CharField(max_length=20, choices=estado_civil,verbose_name='Estado civil')
    direccion = models.CharField(max_length=100,default='',verbose_name='Direccion')
    celular = models.IntegerField(default=934776248)
    correo_electronico = models.EmailField(max_length=50,verbose_name='Correo electrónico',default=' ')
    contrasenia = models.CharField(max_length=35,verbose_name='Contraseña',blank=True)
    
    #Renombrar el objeto
    def __str__(self):
        nombre_completo =self.nombres + " " + self.apellidos
        return nombre_completo

class Especialidad(models.Model):
    codigo_especialidad = models.IntegerField(primary_key=True)
    nombre = models.CharField(default='Neurologia',choices=especialidades,max_length=25)

    class Meta:
        verbose_name_plural = 'Especialidades'
    def __str__(self):
        return self.nombre

class Medico(models.Model):
    persona = models.OneToOneField(Persona,on_delete=models.CASCADE,primary_key=True)
    habilitado = models.BooleanField(default=1)
    especialidad = models.ForeignKey(Especialidad,null=True,blank=True,on_delete=models.RESTRICT)
    horario = models.ForeignKey(Horario,null=True,blank=True,on_delete=models.RESTRICT)


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

