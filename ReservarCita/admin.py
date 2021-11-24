from django.contrib import admin
from django.contrib.admin.decorators import register
from ReservarCita.models import AntecedenteAlergico, AntecedenteFamiliar, AntecedenteGeneral, Especialidad, Horario, Persona,Medico,Paciente, Sede, Seguro,Tecnologo,Cita, Transaccion, Triaje, Turno
# Register your models here.

admin.site.register(Persona)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Tecnologo)
admin.site.register(Cita)
admin.site.register(Especialidad)
admin.site.register(Turno)
admin.site.register(Horario)
admin.site.register(Seguro)
admin.site.register(AntecedenteGeneral)
admin.site.register(AntecedenteFamiliar)
admin.site.register(AntecedenteAlergico)
admin.site.register(Triaje)
admin.site.register(Sede)
admin.site.register(Transaccion)
