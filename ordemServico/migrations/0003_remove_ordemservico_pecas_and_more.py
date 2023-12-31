# Generated by Django 5.0 on 2023-12-27 01:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordemServico', '0002_remove_ordemservico_pecas_and_more'),
        ('servicos', '0004_servico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordemservico',
            name='pecas',
        ),
        migrations.RemoveField(
            model_name='ordemservico',
            name='servico',
        ),
        migrations.DeleteModel(
            name='OrdemServicoPeca',
        ),
        migrations.AddField(
            model_name='ordemservico',
            name='pecas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='servicos.peca'),
        ),
        migrations.AddField(
            model_name='ordemservico',
            name='servico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='servicos.servico'),
        ),
    ]
