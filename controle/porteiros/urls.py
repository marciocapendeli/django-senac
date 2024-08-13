from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # A URL para a página inicial
    path('', views.index, name='home'),

]
