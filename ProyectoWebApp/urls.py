from django.urls import path

from ProyectoWebApp.views import home,servicios,tienda,blog,contacto 

urlpatterns = [
    path('', home, name='home'),
    path('servicios', servicios, name="Servicios"),
    path('tienda', tienda, name="Tienda"),
    path('blog', blog, name="blog"),
    path('contacto', contacto, name="Contacto"),
]