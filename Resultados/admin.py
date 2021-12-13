from django.contrib import admin
from django.urls.resolvers import ResolverMatch

from Resultados.models import Diagnostico, Resonancia, Resultado, Tratamiento

# Register your models here.
admin.site.register(Resonancia)
admin.site.register(Diagnostico)
admin.site.register(Tratamiento)
admin.site.register(Resultado)