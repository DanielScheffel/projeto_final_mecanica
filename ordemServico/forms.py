from django import forms

from . import models

class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = models.OrdemServico
        fields = (
            'veiculo', 'descricao', 'data_inicio', 'data_entrega', 'valor_final'
        )