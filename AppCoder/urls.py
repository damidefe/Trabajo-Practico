from django.urls import path
from AppCoder.views import inicio , carrera , educacion, hobbies 

urlpatterns = [
    path("inicio/", inicio,name = 'inicio'),
    path("carrera/", carrera, name = 'carrera'),
    path("educacion/", educacion, name= 'educacion'),
    path("hobbies/", hobbies, name = 'hobbies'),
]