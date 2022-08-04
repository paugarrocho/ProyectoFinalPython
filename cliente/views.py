from django.shortcuts import render

from cliente.models import Cliente
# Create your views here.

def cliente(request):
    clientes=Cliente.objects.all()
    return render(request, "cliente.html",{"clientes": clientes})
