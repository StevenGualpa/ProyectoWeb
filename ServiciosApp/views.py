from django.shortcuts import render

# Create your views here.

from ServiciosApp.models import Servicio


def servicios(request):
    servicios=Servicio.objects.all() 
    return render(request,"ServiciosApp/servicios.html",{"servicios":servicios})