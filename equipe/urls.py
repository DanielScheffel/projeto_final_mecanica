from django.urls import path
from equipe import views

app_name = 'funcionarios'

urlpatterns = [
    
    #listagens
    path('lista/equipes/', views.equipe, name='equipe'),
    path('lista/funcionarios/', views.funcionario, name='funcionario'),

    # crud
    path('create/equipe/', views.registerEquipe, name='createEquipe'),
    path('equipe/<int:equipe_id>/update/', views.updateEquipe, name='updateEquipe'),

    #crud
    path('create/funcionario/', views.registerFuncionario, name='createFunc'),
    path('funcionario/<int:funcionario_id>/update/', views.updateFuncionario, name='updateFunc'),
]
