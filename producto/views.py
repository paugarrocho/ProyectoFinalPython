from django.shortcuts import render, redirect
from producto.forms import Formulario_producto
from producto.models import Producto
# Create your views here.

def lista_productos(request):
    productos=Producto.objects.all()
    return render(request, "producto/list_producto.html",{"productos": productos})


def nuevo_producto(request):
    
    if request.method == 'POST':
        form = Formulario_producto(request.POST)

        if form.is_valid():
            Producto.objects.create(
                nombre = form.cleaned_data['nombre'],
                stock = form.cleaned_data['stock'],
                precio = form.cleaned_data['precio'],
                categoria = form.cleaned_data['categoria'],
                
            )
            
            return redirect(lista_productos)

    elif request.method == 'GET':
        form = Formulario_producto()
        context = {'form':form}
        return render(request, 'producto/new_producto.html', context=context)

def buscar_producto(request):
    buscar = request.GET['buscar']
    productos = Producto.objects.filter(nombre__icontains=buscar) 
    context = {'productos':productos}
    return render(request, 'producto/buscar_producto.html', context=context)


