from django.shortcuts import render, redirect
from django.urls import reverse
from cliente.forms import ClienteForm

def registerCliente(request):
    form_action = reverse('cliente:create')
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            cliente = form.save()
            return redirect('cliente:create', cliente_id=cliente.pk)
        
        return render(
            request,
            'cliente/cliente_create.html',
            context
        )
    
    context = {
        'form': ClienteForm(),
        'form_action': form_action
    }

    return render(
        request,
        'cliente/cliente_create.html',
        context
    )