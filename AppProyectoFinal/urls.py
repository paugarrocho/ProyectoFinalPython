from django.urls import path
from AppProyectoFinal import views


urlpatterns = [
    path('', views.index, name="index"),
    
]
