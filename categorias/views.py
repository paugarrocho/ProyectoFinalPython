from django.shortcuts import render, redirect
from categorias.forms import Formulario_categorias
from categorias.models import Categorias
# Create your views here.

def lista_categorias(request):
    categoria=Categorias.objects.all()
    return render(request, "categoria/categoria.html",{"categoria": categoria})


def nueva_categoria(request):
    
    if request.method == 'POST':
        form = Formulario_categorias(request.POST)

        if form.is_valid():
            Categorias.objects.create(
                nombre = form.cleaned_data['nombre'],
                clasificacion = form.cleaned_data['clasificacion']
             
            )
            
            return redirect(lista_categorias)

    elif request.method == 'GET':
        form = Formulario_categorias()
        context = {'form':form}
        return render(request, 'cliente/new_categoria.html', context=context)

