
from django.urls import path
from . import views

urlpatterns = [
    
    path('categoria/', views.lista_categorias, name="lista_categorias"),
    path('nueva_categoria/', views.nueva_categoria, name='nueva_categoria')
    

]
