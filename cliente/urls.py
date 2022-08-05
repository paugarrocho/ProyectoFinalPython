
from django.urls import path
from . import views

urlpatterns = [
    
    path('lista_clientes/', views.lista_clientes, name="lista_clientes"),
    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
    

]
