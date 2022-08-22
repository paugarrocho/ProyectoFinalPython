
from django.urls import path
from . import views

urlpatterns = [
    
    path('categoria/', views.lista_categorias, name="lista_categorias"),
    path('nueva_categoria/', views.nueva_categoria, name='nueva_categoria'),
    path('editar_categoria/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('borrar_categoria/<int:pk>/', views.Borrar_categoria.as_view(), name='borrar_categoria'),

]
