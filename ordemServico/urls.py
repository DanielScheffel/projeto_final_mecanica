from django.urls import path
from ordemServico import views

app_name = 'ordem'

urlpatterns = [
    path('home/', views.home, name='home'),

    path('<int:ordemServico_id>/details/', views.detailOrdem, name='detailOrdem'),
    path('create/', views.registerOrdem, name='createOrdem'),
    path('<int:ordemServico_id>/update/', views.updateOrdem, name='updateOrdem'),
    path('<int:ordemServico_id>/delete/', views.deleteOrdem, name='deleteOrdem')
]
