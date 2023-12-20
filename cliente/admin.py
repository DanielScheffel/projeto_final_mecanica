from django.contrib import admin
from cliente import models


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'sobrenome', 'telefone', 'endereco',
    ordering = 'id',


@admin.register(models.Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = 'id', 'placa', 'modelo', 'chassi', 'descricao', 'cliente',