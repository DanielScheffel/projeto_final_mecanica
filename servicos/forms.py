from django import forms
from django.core.exceptions import ValidationError

from . import models

class PecaForm(forms.ModelForm):
    class Meta:
        model = models.Peca
        fields = (
            'nome_peca', 'estoque', 'valor',
        )

class ServicoForm(forms.ModelForm):
    class Meta:
        model = models.Servico
        fields = (
            'nome_servico', 'descricao', 'valor',
        )