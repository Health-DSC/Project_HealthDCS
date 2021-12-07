"""Health_DCS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ReservarCita import views
from Resultados import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index),
    path('iniciarsesion/', views.IniciarSesion, name='iniciarsesion'),
    path('registropaciente/', views.RegistroPaciente),
    
    path('ConfirmarCita/', views.ConfirmarCita),
    path('FechaCita/', views.FechaCita),
    path('MiCuenta/', views.MiCuenta),
    path('MisCitas/', views.MisCitas),
    path('notificaciones/', views.notificaciones),
    path('ConfirmarImagen/', views.ConfirmarImagen),
    path('RecuperoContraseña/', views.RecuperoContraseña),
    path('SubirImagen/', views.SubirImagen),
    path('Especialidades/', views.Especialidades),
    path('Nosotros/', views.Nosotros),
    path('PreguntasFrecuentes/', views.PreguntasFrecuentes),
    path('Reporte/', views.Reporte),
    path('Servicios/', views.Servicios),
    path('Portada/', views.Index),
    path('FinalCita/', views.FinalCita),
    path('MensajeConfirmación/', views.MensajeConfirmación),
    path('AgendarCita/', views.AgendarCita),
    path('agendarcita/elegirmedico/', views.ElegirMedico),
    path('classify/', v.index, name='classify'),
    path('classify/predict', v.classify, name='predict'),

]
