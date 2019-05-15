from django.shortcuts import render
from .models import Aluno

def home(request):
    return render(request, 'home.html', {})

def cadastro(request):
    return render(request, 'cadastro.html', {})
    
def nome(request):
    return render(request, 'nome.html', {})

def ano(request):
    return render(request, 'ano.html', {})

def arena(request):
    return render(request, 'arena.html', {})

def principal(request):
    return render(request, 'principal.html', {})
