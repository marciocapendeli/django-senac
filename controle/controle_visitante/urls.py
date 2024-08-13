
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('porteiros.urls')),  # Inclui as URLs do app porteiros
    path('usuarios/', include('usuarios.urls')),  # Inclui as URLs do app usuarios
]
