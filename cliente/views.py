from django.shortcuts import render, redirect
from cliente.forms import Formulario_clientes
from cliente.models import Cliente
# Create your views here.

def lista_clientes(request):
    clientes=Cliente.objects.all()
    return render(request, "cliente/list_cliente.html",{"clientes": clientes})


def nuevo_clientes(request):
    
    if request.method == 'POST':
        form = Formulario_clientes(request.POST)

        if form.is_valid():
            Cliente.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                stock = form.cleaned_data['stock']
            )
            
            return redirect(lista_clientes)

    elif request.method == 'GET':
        form = Formulario_productos()
        context = {'form':form}
        return render(request, 'products/new_product.html', context=context)

