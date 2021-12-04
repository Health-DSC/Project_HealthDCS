from django.shortcuts import redirect, render
from .models import Persona
from ReservarCita.models import Cita, Especialidad, Medico
from .forms import PersonaForm
from django.http.response import HttpResponse
import django.utils
import datetime

# Create your views here.

def Index(request):
    return render(request, 'Portada.html')

def IniciarSesion(request):
    return render(request, 'IniciarSesion.html')

def RegistroPaciente(request):
    if request.method == 'GET':
        form = PersonaForm()
        contexto = {
            'form':form
        }
    else:
        form = PersonaForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('iniciarsesion')

    return render(request, 'RegistroPaciente.html', contexto)

def AgendarCita(request):
    return render(request, 'AgendarCita.html')

def ConfirmarCita(request):
    return render(request, 'ConfirmarCita.html')

def FechaCita(request):
    return render(request, 'FechaCita.html')

def MiCuenta(request):
    return render(request, 'MiCuenta.html')

def MisCitas(request):
    return render(request, 'MisCitas.html')

def notificaciones(request):
    return render(request, 'notificaciones.html')

def ConfirmarImagen(request):
    return render(request, 'ConfirmarImagen.html')

def RecuperoContraseña(request):
    return render(request, 'RecuperoContraseña.html')

def SubirImagen(request):
    return render(request, 'SubirImagen.html')

def Especialidades(request):
    return render(request, 'Especialidades.html')

def Nosotros(request):
    return render(request, 'Nosotros.html')

def PreguntasFrecuentes(request):
    return render(request, 'PreguntasFrecuentes.html')

def Reporte(request):
    return render(request, 'Reporte.html')

def Servicios(request):
    return render(request, 'Servicios.html')

def FinalCita(request):
    return render(request, 'FinalCita.html')

def MensajeConfirmación(request):
    return render(request, 'MensajeConfirmación.html')

def ElegirMedicoPOST(request):
    medico = request.POST.get('medico')
    fechahora = request.POST.get('fecha_consulta')
    fechahora = django.utils.dateparse.parse_datetime(fechahora)
    hora = fechahora.time()
    fecha = fechahora.date()
    medico = Medico.objects.filter(persona_id=medico)[0]
    Cita.objects.create(fecha=fecha, hora=hora, confirmacion=False, medico=medico)
    return HttpResponse('ok')

def ElegirMedicoGET(request):
    if request.GET["medico"]:
        especialidad=request.GET["especialidad"]
        medico=request.GET["medico"]
        especialidades=Especialidad.objects.filter(nombre=especialidad),
        medicos=Medico.objects.get(Medico(nombre__icontains=medico ) & Medico(especialidad__iexact=especialidades))
        return render(request, "ConfirmarCita.html", {"medicos": medicos, "query": medico})
       
    else:
        especialidad=request.GET["especialidad"]
        especialidades=Especialidad.objects.filter(codigo_especialidad=especialidad)
        especs = [x.codigo_especialidad for x in especialidades]
        medicos=Medico.objects.filter(especialidad__codigo_especialidad__in=especs)
        print(medicos[0])
        return render(request, "ConfirmarCita.html", {"medicos": medicos, "query": especialidad})


def ElegirMedico(request):
    if request.method == "GET":
        return ElegirMedicoGET(request)
    elif request.method == "POST":
        return ElegirMedicoPOST(request)

  