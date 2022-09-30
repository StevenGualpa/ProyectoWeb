from django.contrib import admin
from .models import CategoriasProd,Producto
# Register your models here.

class CategoriasProAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class ProductosAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(CategoriasProd,CategoriasProAdmin)
admin.site.register(Producto,ProductosAdmin)