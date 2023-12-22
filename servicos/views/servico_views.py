from django.shortcuts import render
from servicos.models import Servico

def servico(request):
    servicos = Servico.objects \
        .all().order_by('-id')
    
    context = {
        'servicos': servicos,
        'site_title': 'Serviços - ',
    }

    return render(
        request,
        'servicos/servico.html',
        context
    )