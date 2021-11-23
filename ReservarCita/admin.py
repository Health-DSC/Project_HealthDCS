from django.contrib import admin
from ReservarCita.models import Especialidad, Horario, Persona,Medico,Paciente,Tecnologo,Cita, Turno
# Register your models here.

admin.site.register(Persona)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Tecnologo)
admin.site.register(Cita)
admin.site.register(Especialidad)
admin.site.register(Turno)
admin.site.register(Horario)