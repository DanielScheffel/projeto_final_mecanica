from django.urls import path
from cliente import views

app_name = 'cliente'

urlpatterns = [

    # listagem
    path('', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
    path('lista/cliente/', views.cliente, name='cliente'),
    path('lista/veiculo/', views.veiculo, name='veiculo'),

    # crud cliente
    path('cliente/create/', views.registerCliente, name='create'),

    # crud veiculo
    path('veiculo/create/', views.registerVeiculo, name='createVeiculo'),
]
