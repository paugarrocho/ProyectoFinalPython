
from django.urls import path
from . import views

urlpatterns = [
    
    path('lista_productos/', views.lista_productos, name="lista_productos"),
    path('nuevo_producto/', views.nuevo_producto, name='nuevo_producto'),
    path('buscar_producto/', views.buscar_producto, name='buscar_producto'),
    path('borrar_producto/<int:pk>/', views.Borrar_producto.as_view(), name='borrar_producto'),
    path('editar_producto/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('detalle_producto/<int:pk>/', views.Detalle_producto.as_view(), name='detalle_producto'),
    

]
