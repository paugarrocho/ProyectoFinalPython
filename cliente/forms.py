from django import forms

class Formulario_clientes(forms.Form):
    nombre = forms.CharField(max_length=50)
    direccion = forms.CharField()
    telefono = forms.CharField(max_length=15)
    email = forms.EmailField()


