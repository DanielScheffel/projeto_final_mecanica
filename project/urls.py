
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('cliente.urls')),
    path('servicos/', include('servicos.urls')),
    path('funcionarios/', include('equipe.urls')),
    path('admin/', admin.site.urls),
]
