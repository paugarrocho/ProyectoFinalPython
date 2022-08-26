from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, logout, authenticate

from usuario.forms import Formulario_registro


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

def mostrar_perfil(request):
    if request.user.is_authenticated:
        return HttpResponse(request.user.perfil.telefono)
