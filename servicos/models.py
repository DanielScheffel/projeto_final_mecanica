from django.db import models

class Peca(models.Model):
    nome_peca = models.CharField(max_length=100)
    estoque = models.PositiveIntegerField()
    valor = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self) -> str:
        return self.nome_peca
    
class Servico(models.Model):
    nome_servico = models.CharField(max_length=100)
    descricao = models.TextField(max_length=254)
    valor = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self) -> str:
        return self.nome_servico