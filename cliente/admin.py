from django.contrib import admin
from .models import Cliente
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
	list_display =['nombre', 'direccion', 'telefono', 'email']
	search_fields =['nombre']
	#list_filter = ['tipo']


admin.site.register(Cliente,ClienteAdmin)

