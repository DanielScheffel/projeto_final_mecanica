
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.welcome, name='welcome'),
    path('admin/', admin.site.urls),
    path('clientes/', include('cliente.urls')),
]
