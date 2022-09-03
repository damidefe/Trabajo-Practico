
from django.shortcuts import render ,HttpResponse
from AppCoder.models import Familiar 
from django.template  import  loader
from datetime import datetime





def familiares(request):
    fecha_actual = datetime.now()
    familiares = Familiar.objects.all()
    return render(request, "familiares.html", {'familiares':familiares , "fecha_actual" : fecha_actual },  )

def inicio(request):
    return render(request, "inicio.html",   )
