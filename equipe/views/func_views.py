from django.shortcuts import render
from equipe.models import Funcionario

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