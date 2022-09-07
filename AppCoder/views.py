
from django.shortcuts import render ,HttpResponse
from AppCoder.models import Familiar 
from django.template  import  loader
from datetime import datetime





def carrera(request):
    fecha_actual = datetime.now()
    carrera = Familiar.objects.all()
    return render(request, "AppCoder/carrera.html", {'carrera':carrera , "fecha_actual" : fecha_actual },  )

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def educacion(request):
    return render(request, "AppCoder/educacion.html")

def hobbies(request):
    return render(request, "AppCoder/hobbies.html")
