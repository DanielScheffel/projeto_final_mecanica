from django.shortcuts import render
from cliente.models import Cliente, Veiculo

def welcome(request):
    return render(
        request,
        'cliente/welcome.html'
    )

def home(request):
    return render(request, "cliente/home.html");

def cliente(request):
    clientes = Cliente.objects \
        .all().order_by('-id')
    
    context = {
        'clientes': clientes,
        'site_title': 'Clientes - ',
    }

    return render(
        request, 
        "cliente/cliente.html", 
        context
    )

def veiculo(request):
    veiculos = Veiculo.objects \
        .all().order_by('-id')
    
    context = {
        'veiculos': veiculos,
        'site_title': 'Veiculos - ',
    }

    return render(
        request, 
        "veiculo/veiculo.html", 
        context
    )