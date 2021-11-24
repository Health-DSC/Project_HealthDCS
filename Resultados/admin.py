from django.contrib import admin
from django.urls.resolvers import ResolverMatch

from Resultados.models import Diagnostico, Imagen, Recurso, Resonancia, Resultado, Tratamiento

# Register your models here.
admin.site.register(Recurso)
admin.site.register(Resonancia)
admin.site.register(Imagen)
admin.site.register(Diagnostico)
admin.site.register(Tratamiento)
admin.site.register(Resultado)