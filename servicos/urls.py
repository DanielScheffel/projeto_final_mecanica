from django.urls import path
from servicos import views

app_name = 'servicos'

urlpatterns = [

    # listagens
    path('lista/pecas/', views.peca, name='pecas'),

    # Crud peças
    path('peca/create/', views.registerPeca, name='createPeca'),
]
