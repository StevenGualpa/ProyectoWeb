
from django.urls import path

from .views import blog,categoria
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', blog, name="Blog"),
    path('categoria/<int:categoria_id>', categoria, name="Categoria"),

]