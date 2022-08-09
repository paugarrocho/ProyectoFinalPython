
from django.urls import path
from . import views

urlpatterns = [
    
    path('lista_productos/', views.lista_productos, name="lista_productos"),
    path('nuevo_producto/', views.nuevo_producto, name='nuevo_producto'),
    path('buscar_producto/', views.buscar_producto, name='buscar_producto'),
    

]
