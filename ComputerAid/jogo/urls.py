from django.urls import path
from . import views

app_name = 'jogo'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('nome/', views.nome, name='nome'),
    path('ano/', views.ano, name='ano'),
    path('arena/', views.arena, name='arena'),
    path('principal/', views.principal, name='principal'),
]