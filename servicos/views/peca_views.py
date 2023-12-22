from django.shortcuts import render
from servicos.models import Peca

def peca(request):
    pecas = Peca.objects \
        .all().order_by('-id')
    
    context = {
        'pecas': pecas,
        'site_title': 'Peças - ',
    }

    return render(
        request,
        'pecas/pecas.html',
        context
    )