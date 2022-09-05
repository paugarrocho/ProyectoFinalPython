from django.urls import path
from . import views
from usuario.views import mostrar_perfil, pedido_entrada, registrar, editar_usuario, Detalle_usuario
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('lista_usuarios/', views.lista_usuarios, name="lista_usuarios"),
    path('entrar/', pedido_entrada, name='entrar'),
    path('registrar/', registrar, name='registrar'),
    path('salir/', LogoutView.as_view(template_name = 'index.html'), name='salir'),
    path('perfil/', mostrar_perfil, name='perfil'),
    path('editar_usuario/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('detalle_usuario/<int:pk>/', Detalle_usuario.as_view(), name='detalle_usuario'),
    
]