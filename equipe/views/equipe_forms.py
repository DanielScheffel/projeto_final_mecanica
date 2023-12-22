from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from equipe.forms import EquipeForm
from equipe.models import Equipe

def registerEquipe(request):
    form_action = reverse('funcionarios:createEquipe')
    if request.method == 'POST':
        form = EquipeForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            equipe = form.save()
            return redirect('funcionarios:equipe')
        
        return render(
            request,
            'equipe/equipe_create.html',
            context
        )
    
    context = {
        'form': EquipeForm(),
        'form_action': form_action
    }

    return render(
        request,
        'equipe/equipe_create.html',
        context
    )

def updateEquipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)
    form_action = reverse('funcionarios:updateEquipe', args=(equipe_id,))
    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=equipe)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            form.save()
            return redirect('funcionarios:equipe')
        
        return render(
            request,
            'equipe/equipe_create.html',
            context
        )
    
    context = {
        'form': EquipeForm(instance=equipe),
        'form_action': form_action
    }

    return render(
        request,
        'equipe/equipe_create.html',
        context
    )

