from django.urls import path
from servicos import views

app_name = 'servicos'

urlpatterns = [

    # listagens
    path('lista/pecas/', views.peca, name='pecas'),
    path('lista/servicos/', views.servico, name='servicos'),

    # Crud peças
    path('peca/create/', views.registerPeca, name='createPeca'),
    path('peca/<int:peca_id>/update/', views.updatePeca, name='updatePeca'),

    # Crud Serviços
    path('servicos/create/', views.resgisterServico, name='createServico'),
    path('servicos/<int:servico_id>/update', views.updateServico, name='updateServico'),
]
