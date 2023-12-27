from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from ordemServico.forms import OrdemServicoForm
from ordemServico.models import OrdemServico
from decimal import Decimal
from cliente.models import Veiculo

def home(request):
    ordens = OrdemServico.objects \
        .all().order_by('-id')
    
    context = {
        'ordens': ordens,
        'site_title': 'Ordem Serviço - ',
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

def updateOrdem(request, ordemServico_id):
    ordem = get_object_or_404(OrdemServico, pk=ordemServico_id)
    form_action = reverse('ordem:updateOrdem', args=(ordemServico_id,))
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST, instance=ordem)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            form.save()
            return redirect('ordem:detailsOrdem')
        
        return render(
            request,
            'ordem/ordem_create.html',
            context
        )
    
    context = {
        'form': OrdemServicoForm(instance=ordem),
        'form_action': form_action
    }

    return render(
        request,
        'ordem/ordem_create.html',
        context
    )

def deleteOrdem(request, ordemServico_id):
    ordem = get_object_or_404(OrdemServico, pk=ordemServico_id)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        ordem.delete()
        return redirect('ordem:home')
    
    return render(
        request,
        'ordem/ordem_detail.html',
        {
            'ordem': ordem,
            'confirmation': confirmation
        }
    )

def concluirOrdem(request, ordemServico_id):
    ...

def detailOrdem(request, ordemServico_id):
    ordem = get_object_or_404(OrdemServico, pk=ordemServico_id)
    # veiculo = Veiculo.objects.get(placa=ordem.placa)
    veiculo = ordem.veiculo

    site_title = f'{veiculo.placa}'

    context = {
        'ordem': ordem,
        'veiculo': veiculo,
        'site_title': site_title
    }

    return render(
        request,
        'ordem/ordem_detail.html',
        context
    )