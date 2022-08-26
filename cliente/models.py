from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=15)
    email=models.EmailField()
    
    
    

    class Meta:
        verbose_name="Cliente"
        verbose_name_plural="Clientes"
    
    def __str__(self):
        return self.nombre