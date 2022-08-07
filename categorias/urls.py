
from django.urls import path
from . import views

urlpatterns = [
    
    path('lista_categorias/', views.lista_categorias, name="lista_categorias"),
    path('nueva_categoria/', views.nueva_categoria, name='nueva_categoria')
    

]
