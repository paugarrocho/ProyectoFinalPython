from tkinter import CASCADE
from django.db import models
from categorias.models import Categorias

# Create your models here.

class Producto(models.Model):
    
    nombre=models.CharField(max_length=50)
    stock=models.IntegerField()
    precio=models.FloatField()
    categoria=models.ForeignKey(Categorias, on_delete=models.CASCADE)
    disponibilidad=models.BooleanField(default=True)
    
    

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
    
    def __str__(self):
        return self.nombre
