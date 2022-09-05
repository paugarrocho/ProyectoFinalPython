from http.client import HTTPResponse
from django.shortcuts import render, redirect
from producto.forms import Formulario_producto
from producto.models import Producto
from django.views.generic import  DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def lista_productos(request):
    productos=Producto.objects.all()
    return render(request, "producto/list_producto.html",{"productos": productos})


@login_required
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

def editar_producto(request, pk):
    if request.method == 'POST':
        form = Formulario_producto(request.POST)
        if form.is_valid():
            producto = Producto.objects.get(id=pk)
            producto.nombre = form.cleaned_data['nombre']
            producto.stock = form.cleaned_data['stock']
            producto.precio =  form.cleaned_data['precio']
            producto.categoria = form.cleaned_data['categoria']
            producto.save()

            return redirect(lista_productos)


    elif request.method == 'GET':
        producto = Producto.objects.get(id=pk)

        form = Formulario_producto(initial={
                                        'nombre':producto.nombre,
                                        'stock':producto.stock, 
                                        'precio':producto.precio,
                                        'categoria':producto.categoria})
        context = {'form':form}
        return render(request, 'producto/editar_producto.html', context=context)

class Borrar_producto(LoginRequiredMixin,DeleteView):
    model = Producto
    template_name = 'producto/borrar_producto.html'
    success_url = '/producto/list_productos/'

class Detalle_producto(LoginRequiredMixin,DetailView):
    model = Producto
    template_name = 'producto/detalle_producto.html'

    

       

        
        
