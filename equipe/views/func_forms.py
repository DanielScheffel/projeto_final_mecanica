from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from equipe.forms import FuncForm
from equipe.models import Funcionario

def registerFuncionario(request):
    form_action = reverse('funcionarios:createFunc')
    if request.method == 'POST':
        form = FuncForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            funcionario = form.save()
            return redirect('funcionarios:funcionario')
        
        return render(
            request,
            'funcionarios/func_create.html',
            context
        )
    
    context = {
        'form': FuncForm(),
        'form_action': form_action
    }

    return render(
        request,
        'funcionarios/func_create.html',
        context
    )

def updateFuncionario(request, funcionario_id):
    equipe = get_object_or_404(Funcionario, pk=funcionario_id)
    form_action = reverse('funcionarios:updateFunc', args=(funcionario_id,))
    if request.method == 'POST':
        form = FuncForm(request.POST, instance=equipe)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            form.save()
            return redirect('funcionarios:funcionario')
        
        return render(
            request,
            'equipe/func_create.html',
            context
        )
    
    context = {
        'form': FuncForm(instance=equipe),
        'form_action': form_action
    }

    return render(
        request,
        'equipe/Func_create.html',
        context
    )