from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from cliente.forms import VeiculoForm
from cliente.models import Veiculo

def registerVeiculo(request):
    form_action = reverse('cliente:createVeiculo')
    if request.method == 'POST':
        form = VeiculoForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            veiculo = form.save()
            return redirect('cliente:veiculo')
        
        return render(
            request,
            'veiculo/veiculo_create.html',
            context
        )
    
    context = {
        'form': VeiculoForm(),
        'form_action': form_action
    }

    return render(
        request,
        'veiculo/veiculo_create.html',
        context
    )

def updateVeiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, pk=veiculo_id)
    form_action = reverse('cliente:updateVeiculo', args=(veiculo_id,))
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            form.save()
            return redirect('cliente:veiculo')
        
        return render(
            request,
            'veiculo/veiculo_create.html',
            context
        )
    
    context = {
        'form': VeiculoForm(instance=veiculo),
        'form_action': form_action
    }

    return render(
        request,
        'veiculo/veiculo_create.html',
        context
    )