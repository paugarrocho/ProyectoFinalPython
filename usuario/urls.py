from django.urls import path

from usuario.views import mostrar_perfil, pedido_entrada, registrar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('entrar/', pedido_entrada, name='entrar'),
    path('registrar/', registrar, name='registrar'),
    path('salir/', LogoutView.as_view(template_name = 'index.html'), name='salir'),
    path('perfil/', mostrar_perfil, name='perfil'),
]