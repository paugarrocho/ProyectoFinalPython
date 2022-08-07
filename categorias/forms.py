from django import forms

class Formulario_categorias(forms.Form):
    nombre = forms.CharField(max_length=50)
    clasificacion = forms.CharField(max_length=50)
