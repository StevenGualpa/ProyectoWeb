from xml.dom.minidom import Document
from django.urls import path

from .views import servicios
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', servicios, name="Servicios"),
]