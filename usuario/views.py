

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from .models import Perfil_usuario
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views.generic import  DetailView
from django.contrib.auth.decorators import login_required
from usuario.forms import Formulario_registro, Formulario_usuario


@login_required
def lista_usuarios(request):
    usuarios=User.objects.all()
    return render(request, "usuario/lista_usuarios.html",{"usuarios": usuarios})


def pedido_entrada(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                
                context = {'message':f'Bienvenido {username}!! :D'}
                return render(request, 'index.html', context = context)

        form = AuthenticationForm()
        return render(request, 'usuario/entrar.html', {'error': 'Formulário inválido', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'usuario/entrar.html', {'form': form})

def registrar(request):
    if request.method == 'POST':
        
        form = Formulario_registro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entrar')
        else:
            context = {'errors':form.errors}
            form = Formulario_registro()
            context['form'] = form
            return render(request, 'usuario/registrar.html', context)

    elif request.method == 'GET':
        form = Formulario_registro()
        return render(request, 'usuario/registrar.html', {'form': form})

@login_required
def mostrar_perfil(request):
    
    if request.user.is_authenticated:
        return render(request,'usuario/perfil.html')

@login_required
def editar_usuario(request, pk):
    if request.method == 'POST':
        form = Formulario_usuario(request.POST, request.FILES)
        
        if form.is_valid():
            usuario = Perfil_usuario.objects.get(id=pk)
            usuario.direccion = form.cleaned_data['direccion']
            usuario.telefono = form.cleaned_data['telefono']
            usuario.imagen = form.cleaned_data['imagen']
            usuario.save()
                    
        return redirect('index')

    elif request.method == 'GET':
        usuario = Perfil_usuario.objects.get(id=pk)
        form = Formulario_usuario(initial={
                                        'direccion':usuario.direccion, 
                                        'telefono':usuario.telefono,
                                        'imagen':usuario.imagen})
        context = {'form':form}
        return render(request, 'usuario/editar_usuario.html', context=context)    



class Detalle_usuario(DetailView):
    model = Perfil_usuario
    template_name = 'usuario/detalle_usuario.html'
    


    
    



