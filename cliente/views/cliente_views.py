from django.shortcuts import render, get_object_or_404
from cliente.models import Cliente, Veiculo

def welcome(request):
    return render(
        request,
        'cliente/welcome.html',
    )

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

def cardCliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    veiculos = Veiculo.objects.filter(cliente=cliente)

    site_title = f'{cliente.nome} {cliente.sobrenome} - '

    context = {
        'cliente': cliente,
        'veiculos': veiculos,
        'site_title': site_title
    }

    return render(
        request,
        'cliente/cliente_detail.html',
        context
    )