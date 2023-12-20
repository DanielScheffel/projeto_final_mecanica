from django.shortcuts import render, redirect
from django.urls import reverse
from cliente.forms import VeiculoForm

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
            return redirect('cliente:veiculo', veiculo_id=veiculo.pk)
        
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