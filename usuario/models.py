from django.db import models
from django.contrib.auth.models import User

class Perfil_usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to='perfil_imagen',  null=True, blank=True)

    def __str__(self):
        return self.usuario.username + ' - perfil'