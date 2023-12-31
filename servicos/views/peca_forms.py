from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from servicos.forms import PecaForm
from servicos.models import Peca

def registerPeca(request):
    form_action = reverse('servicos:createPeca')
    if request.method == 'POST':
        form = PecaForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            peca = form.save()
            return redirect('servicos:pecas')
        
        return render(
            request,
            'pecas/peca_create.html',
            context
        )
        
    context = {
        'form': PecaForm(),
        'form_action': form_action
    }

    return render(
        request,
        'pecas/peca_create.html',
        context
    )

def updatePeca(request, peca_id):
    peca = get_object_or_404(Peca, pk=peca_id)
    form_action = reverse('servicos:updatePeca', args=(peca_id,))
    if request.method == 'POST':
        form = PecaForm(request.POST, instance=peca)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            form.save()
            return redirect('servicos:pecas')
        
        return render(
            request,
            'pecas/peca_create.html',
            context
        )
    
    context = {
        'form': PecaForm(instance=peca),
        'form_action': form_action
    }

    return render(
        request,
        'pecas/peca_create.html',
        context
    )