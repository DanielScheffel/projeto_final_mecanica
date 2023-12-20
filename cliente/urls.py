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
    path('cliente/<int:cliente_id>/detail/', views.cardCliente, name='cardCliente'),
    path('cliente/create/', views.registerCliente, name='create'),
    path('cliente/<int:cliente_id>/update/', views.updateCliente, name='update'),
    path('cliente/<int:cliente_id>/delete/', views.delete, name='delete'),

    # crud veiculo
    path('veiculo/create/', views.registerVeiculo, name='createVeiculo'),
    path('veiculo/<int:veiculo_id>/update/', views.updateVeiculo, name='updateVeiculo'),
]
