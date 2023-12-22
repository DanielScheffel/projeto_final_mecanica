from django.shortcuts import render, get_object_or_404
from equipe.models import Funcionario, Equipe

def funcionario(request):
    funcionarios = Funcionario.objects \
        .all().order_by('-id')
    
    context = {
        'funcionarios': funcionarios,
        'site_title': 'Funcionários - ',
    }

    return render(
        request,
        'funcionarios/funcionario.html',
        context
    )

def detailFunc(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
    equipes = Equipe.objects.filter(funcionario=funcionario)

    site_title = f'{funcionario.nome} {funcionario.sobrenome}'

    context = {
        'funcionario': funcionario,
        'equipes': equipes,
        'site_title': site_title
    }

    return render(
        request,
        'funcionarios/func_detail.html',
        context
    )