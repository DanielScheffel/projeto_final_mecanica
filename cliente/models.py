from django.db import models


from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=50)
    endereco = models.CharField(max_length=254, blank=True)

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'

class Veiculo(models.Model):
    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'

    placa = models.CharField(max_length=7)
    modelo = models.CharField(max_length=50)
    chassi = models.CharField(max_length=50)
    descricao = models.CharField(max_length=254, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.placa