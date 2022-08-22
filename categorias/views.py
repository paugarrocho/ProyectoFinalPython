from calendar import c
from django.shortcuts import render, redirect
from categorias.forms import Formulario_categorias
from categorias.models import Categorias
from django.views.generic import  DeleteView
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
        return render(request, 'categoria/new_categoria.html', context=context)
    
    
def editar_categoria(request, pk):
    if request.method == 'POST':
        form = Formulario_categorias(request.POST)
        if form.is_valid():
            categoria= Categorias.objects.get(id=pk)
            categoria.nombre = form.cleaned_data['nombre']
            categoria.clasificacion = form.cleaned_data['clasificacion']
            categoria.save()
            
            return redirect(lista_categorias)
        
    elif request.method == 'GET':
        categoria = Categorias.objects.get(id=pk)
            
        form = Formulario_categorias(initial={
                                            'nombre':categoria.nombre,
                                            'clasificacion':categoria.clasificacion})
            
        context = {'form':form}
        return render(request, 'categoria/editar_categoria.html', context=context)


class Borrar_categoria(DeleteView):
    model = Categorias
    template_name = 'categoria/borrar_categoria.html'
    success_url = '/categoria/categoria/'

