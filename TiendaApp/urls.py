from django.urls import path

from .views import tienda
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', tienda, name="Tienda"),
]