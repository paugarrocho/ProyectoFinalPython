from django.contrib import admin

from email.mime import image


from usuario.models import Perfil_usuario

@admin.register(Perfil_usuario)
class Perfil_usuario_admin(admin.ModelAdmin):
    list_display = ['usuario', 'telefono', 'direccion', 'imagen']

