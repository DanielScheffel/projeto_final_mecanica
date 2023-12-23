from django.shortcuts import render, redirect
from django.urls import reverse
from ordemServico.forms import OrdemServicoForm
from ordemServico.models import OrdemServico

def home(request):
    ordens = OrdemServico.objects \
        .all().order_by('-id')
    
    context = {
        'ordens': ordens,
        'site_title': 'Equipes - ',
    }
    return render(request, "ordem/home.html", context)

def registerOrdem(request):
    form_action = reverse('ordem:createOrdem')
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)

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