from django import forms
from categorias.models import Categorias

class Formulario_producto(forms.Form):
    nombre = forms.CharField(max_length=50)
    stock = forms.IntegerField()
    precio = forms.FloatField()
    categoria=forms.ModelChoiceField(queryset=Categorias.objects.all())
    


