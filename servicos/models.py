from django.db import models

class Peca(models.Model):
    nome_peca = models.CharField(max_length=50)
    quantidade = models.PositiveIntegerField()
    valor = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self) -> str:
        return self.nome_peca