from unicodedata import name
from django.conf import settings
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from ProyectoWeb.settings import EMAIL_HOST_USER,MEDIA_ROOT
from BlogApp.models import Post
import os
# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            subject="Mensaje Enviado desde App Django"
            message="El usuario con nombre {} con la direccion {} escribe lo siguiente:".format(nombre,contenido)
            email_from=EMAIL_HOST_USER
            #recipient_list=["stevengualpa@hotmail.com","rino.arias2018@uteq.edu.ec","jorge.gualpa2015@uteq.edu.ec"]
            recipient_list=[email]
            #sas=Post.objects.first()
            sas1=Post.objects.get(imagen="blog/descarga.jpg")
            #ruta=os.path.join(MEDIA_ROOT,sas.imagen.name.replace("/","\\"))
            print('esta es la direccin?'+sas1.imagen.name)
            try:
                email1=EmailMessage(subject=subject,body=message,from_email=email_from,to=recipient_list)
                email1.attach('Holaaaaaa.png', sas1.imagen.read(), 'image/png')
                email1.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
    return render(request,"ContactoApp/contacto.html",{'miformulario':formulario_contacto})