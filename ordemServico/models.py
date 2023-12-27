from django.db import models
from cliente.models import Cliente, Veiculo
from equipe.models import Equipe
from servicos.models import Servico, Peca

class OrdemServico(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField(max_length=254)
    data_inicio = models.DateField()
    data_entrega = models.DateField(null=True)
    equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True)
    servico = models.ManyToManyField(Servico, null=True)
    pecas = models.ManyToManyField(Peca, null=True)
    valor_final = models.DecimalField(decimal_places=2, max_digits=8, null=True)
