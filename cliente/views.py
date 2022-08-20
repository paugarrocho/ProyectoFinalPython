from django.shortcuts import render, redirect
from cliente.forms import Formulario_clientes
from cliente.models import Cliente
from django.views.generic import  DeleteView
# Create your views here.

def lista_clientes(request):
    clientes=Cliente.objects.all()
    return render(request, "cliente/list_cliente.html",{"clientes": clientes})


def nuevo_cliente(request):
    
    if request.method == 'POST':
        form = Formulario_clientes(request.POST)

        if form.is_valid():
            Cliente.objects.create(
                nombre = form.cleaned_data['nombre'],
                direccion = form.cleaned_data['direccion'],
                telefono = form.cleaned_data['telefono'],
                email = form.cleaned_data['email']
            )
            
            return redirect(lista_clientes)

    elif request.method == 'GET':
        form = Formulario_clientes()
        context = {'form':form}
        return render(request, 'cliente/new_cliente.html', context=context)

def buscar_cliente(request):
    buscar = request.GET['buscar']
    clientes = Cliente.objects.filter(nombre__icontains=buscar) 
    context = {'clientes':clientes}
    return render(request, 'cliente/buscar_cliente.html', context=context)


def editar_cliente(request, pk):
    if request.method == 'POST':
        form = Formulario_clientes(request.POST)
        if form.is_valid():
            cliente = Cliente.objects.get(id=pk)
            cliente.nombre = form.cleaned_data['nombre']
            cliente.direccion = form.cleaned_data['direccion']
            cliente.telefono = form.cleaned_data['telefono']
            cliente.email = form.cleaned_data['email']
            cliente.save()

            return redirect(lista_clientes)


    elif request.method == 'GET':
        cliente = Cliente.objects.get(id=pk)

        form = Formulario_clientes(initial={
                                        'nombre':cliente.nombre,
                                        'direccion':cliente.direccion, 
                                        'telefono':cliente.telefono,
                                        'email':cliente.email})
        context = {'form':form}
        return render(request, 'cliente/editar_cliente.html', context=context)


class Borrar_cliente(DeleteView):
    model = Cliente
    template_name = 'cliente/borrar_cliente.html'
    success_url = '/cliente/lista_clientes/'



