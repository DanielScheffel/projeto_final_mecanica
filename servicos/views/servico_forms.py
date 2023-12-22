from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from servicos.forms import ServicoForm
from servicos.models import Servico


def resgisterServico(request):
    form_action = reverse('servicos:createServico')
    if request.method == 'POST':
        form = ServicoForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            servico = form.save()
            return redirect('servicos:servicos')
        
        return render(
            request,
            'servicos/servico_create.html',
            context
        )
    
    context = {
        'form': ServicoForm(),
        'form_action': form_action
    }

    return render(
        request,
        'servicos/servico_create.html',
        context
    )

def updateServico(request, servico_id):
    servico = get_object_or_404(Servico, pk=servico_id)
    form_action = reverse('servicos:updateServico', args=(servico_id,))
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            form.save()
            return redirect('servicos:servicos')
        
        return render(
            request,
            'servicos/servico_create.html',
            context
        )
    
    context = {
        'form': ServicoForm(instance=servico),
        'form_action': form_action
    }

    return render(
        request,
        'servicos/servico_create.html',
        context
    )