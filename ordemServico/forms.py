from django import forms

from . import models
from servicos.models import Servico, Peca

class OrdemServicoForm(forms.ModelForm):
    valor_final = forms.DecimalField(label='Valor Total', required=False)
    class Meta:
        model = models.OrdemServico
        fields = (
            'veiculo', 'descricao', 'data_inicio', 'equipe', 'servico', 'pecas',
        )