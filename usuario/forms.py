
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from usuario.models import Perfil_usuario

class Formulario_registro(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        help_texts = {k:'' for k in fields}


# class Formulario_usuario(forms.Form):
#     telefono = forms.CharField(required=False)
#     direccion = forms.CharField(max_length=50,required=False)
#     imagen = forms.ImageField(required=False)

class Formulario_usuario(ModelForm):

    class Meta:
        model = Perfil_usuario
        fields = ('usuario','telefono', 'direccion', 'imagen')