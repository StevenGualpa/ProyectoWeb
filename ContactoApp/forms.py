import email
from django import forms
from pkg_resources import require

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre",required=True)

    email=forms.CharField(label='Correo', required=True, max_length=100)

    contenido=forms.CharField(label="Contenido",widget=forms.Textarea)