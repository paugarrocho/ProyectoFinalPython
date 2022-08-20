from django.contrib import admin

from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
	list_display =['nombre', 'stock', 'precio', 'categoria']
	search_fields =['nombre']
	list_filter = ['categoria']


admin.site.register(Producto, ProductoAdmin)
