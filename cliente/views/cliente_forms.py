from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from cliente.forms import ClienteForm
from cliente.models import Cliente

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
            return redirect('cliente:cliente')
        
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

def updateCliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    form_action = reverse('cliente:update', args=(cliente_id,))
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            form.save()
            return redirect('cliente:update', cliente_id=cliente.pk)
        
        return render(
            request,
            'cliente/cliente_create.html',
            context
        )
    
    context = {
        'form': ClienteForm(instance=cliente),
        'form_action': form_action
    }

    return render(
        request,
        'cliente/cliente_create.html',
        context
    )

def delete(request, cliente_id):
    cliente = get_object_or_404(
        Cliente, pk=cliente_id
    )

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        cliente.delete()
        # veiculos = Veiculo.objects.filter(cliente=cliente)
        # veiculos.delete()
        return redirect('cliente:cliente')
    
    return render(
        request,
        'cliente/cliente_detail.html',
        {
            'cliente': cliente,
            'confirmation': confirmation
        }
    )