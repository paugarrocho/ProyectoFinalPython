
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.cliente, name="Cliente"),
    

]