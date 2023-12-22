from django.urls import path
from ordemServico import views

app_name = 'ordem'

urlpatterns = [
    path('home/', views.home, name='home'),

    path('create/', views.registerOrdem, name='createOrdem'),
]
