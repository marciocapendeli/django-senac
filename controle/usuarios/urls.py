# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Mapeia a URL principal do app para a view `index`
    path('', views.index, name='home'),
]
