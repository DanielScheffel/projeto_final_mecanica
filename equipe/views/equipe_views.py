from django.shortcuts import render
from equipe.models import Equipe

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

def equipeDetail(request):
    ...