from django.shortcuts import render, redirect
from django.urls import reverse
from ordemServico.forms import OrdemServicoForm
from ordemServico.models import OrdemServico

def home(request):
    return render(request, "ordem/home.html")

def registerOrdem(request):
    form_action = reverse('ordem:createOrdem')
    if request.method == 'POST':
        form = OrdemServico(request.POST)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            ordem = form.save()
            return redirect('ordem:home')
        
        return render(
            request,
            'ordem/ordem_create.html',
            context
        )
    
    context = {
        'form': OrdemServicoForm(),
        'form_action': form_action
    }

    return render(
        request,
        'ordem/ordem_create.html',
        context
    )