from django.db import models


class Equipe(models.Model):
    nome_equipe = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome_equipe
    
class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=12)
    # telefone = models.CharField(max_length=50)
    equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'