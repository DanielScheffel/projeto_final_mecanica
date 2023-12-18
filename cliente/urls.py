from django.urls import path
from cliente import views

urlpatterns = [
    path('', views.home, name='home'),
]
