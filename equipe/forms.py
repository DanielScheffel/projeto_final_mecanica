from django import forms
from django.core.exceptions import ValidationError

from . import models

class EquipeForm(forms.ModelForm):
    class Meta:
        model = models.Equipe
        fields = (
            'nome_equipe', 'especialidade'
        )

class FuncForm(forms.ModelForm):
    class Meta:
        model = models.Funcionario
        fields = (
            'nome', 'sobrenome', 'email', 'cpf', 'equipe'
        )