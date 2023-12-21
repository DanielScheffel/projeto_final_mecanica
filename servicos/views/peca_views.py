from django.shortcuts import render

def peca(request):
    return render(
        request,
        'pecas/pecas.html',
    )