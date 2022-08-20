
from django.urls import path
from . import views
from cliente.views import Borrar_cliente

urlpatterns = [
    
    path('lista_clientes/', views.lista_clientes, name="lista_clientes"),
    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
    path('buscar_cliente/', views.buscar_cliente, name='buscar_cliente'),
    path('borrar_cliente/<int:pk>/', Borrar_cliente.as_view(), name='borrar_cliente'),
    path('editar_cliente/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    

]
