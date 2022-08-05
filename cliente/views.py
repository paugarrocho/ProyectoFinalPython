from django.shortcuts import render, redirect
from cliente.forms import Formulario_clientes
from cliente.models import Cliente
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

