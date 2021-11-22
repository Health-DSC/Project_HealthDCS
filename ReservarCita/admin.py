from django.contrib import admin
from ReservarCita.models import Persona,Medico,Paciente,Tecnologo,Cita
# Register your models here.

admin.site.register(Persona)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Tecnologo)
admin.site.register(Cita)