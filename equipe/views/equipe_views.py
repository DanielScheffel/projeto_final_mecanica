from django.shortcuts import render, get_object_or_404
from equipe.models import Equipe, Funcionario

def equipe(request):
    equipes = Equipe.objects \
        .all().order_by('-id')
    
    context = {
        'equipes': equipes,
        'site_title': 'Equipes - ',
    }

    return render(
        request,
        'equipe/equipe.html',
        context
    )

def equipeDetail(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)
    funcionarios = Funcionario.objects.filter(equipe=equipe)

    site_title = f'{equipe.nome_equipe}'

    context = {
        'equipe': equipe,
        'funcionarios': funcionarios,
        'site_title': site_title
    }

    return render(
        request,
        'equipe/equipe_detail.html',
        context
    )