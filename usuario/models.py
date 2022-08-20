from django.db import models

class Perfil_usuario(models.Model):
    usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='perfil')
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    imagen = models.ImageField(upload_to='perfil_imagen/', blank=True)

    def __str__(self):
        return self.user.username + ' - perfil'