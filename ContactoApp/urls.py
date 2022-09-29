from django.urls import path

from .views import contacto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', contacto, name="Contacto"),
]