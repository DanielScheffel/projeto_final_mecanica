from django.urls import path
from equipe import views

app_name = 'funcionarios'

urlpatterns = [
    
    #listagens
    path('lista/equipes/', views.equipe, name='equipe'),
    path('lista/funcionarios/', views.funcionario, name='funcionario'),

    # crud
    path('equipe/<int:equipe_id>/detail/', views.equipeDetail, name='detailEquipe'),
    path('create/equipe/', views.registerEquipe, name='createEquipe'),
    path('equipe/<int:equipe_id>/update/', views.updateEquipe, name='updateEquipe'),
    path('equipe/<int:equipe_id>/delete/', views.deleteEquipe, name='deleteEquipe'),

    #crud
    path('funcionario/<int:funcionario_id>/detail/', views.detailFunc, name='detailFunc'),
    path('create/funcionario/', views.registerFuncionario, name='createFunc'),
    path('funcionario/<int:funcionario_id>/update/', views.updateFuncionario, name='updateFunc'),
    path('funcionario/<int:funcionario_id>/delete/', views.deleteFunc, name='deleteFunc'),
]
