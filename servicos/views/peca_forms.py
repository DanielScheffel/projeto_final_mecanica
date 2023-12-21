from django.shortcuts import render
from servicos.forms import PecaForm

def registerPeca(request):
    form = PecaForm()

    context = {
        'form': form,
    }

    return render(
        request,
        'pecas/peca_create.html',
        context,
    )