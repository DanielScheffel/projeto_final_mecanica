from django import forms
from django.core.exceptions import ValidationError

from . import models

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = (
            'nome', 'sobrenome', 'telefone', 'endereco'
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome')
        sobrenome = cleaned_data.get('sobrenome')

        if nome == sobrenome:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )

            self.add_error('nome', msg)
            self.add_error('sobrenome', msg)

        return super().clean()
    
    def clean_names(self):
        nome = self.cleaned_data.get('nome')
        sobrenome = self.cleaned_data.get('sobrenome')

        if nome or sobrenome == 'ABC':
            self.add_error(
                'nome',
                'sobrenome',
                ValidationError(
                    'Não é permitido esses caracteres...',
                    code='invalid'
                )
            )

        return nome, sobrenome

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = models.Veiculo
        fields = (
            'placa', 'modelo', 'chassi', 'descricao', 'cliente'
        )