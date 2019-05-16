from django.shortcuts import render
from .models import Aluno

def home(request):
    return render(request, 'home.html', {})

def login(request):
    return render(request, 'principal.html', {})

def nome(request):
    return render(request, 'nome.html', {})

def Cadnome(request):
    nome = request.POST.get('nome')
    nick = request.POST.get('nick')
    senha = request.POST.get('senha')
    pontuacao = 0
    nivel = 1
    moedas = 0
    ano = 0
    
    try:
        Aluno.object.create(nome=nome,nick=nick,senha=senha,pontuacao=pontuacao,nivel=nivel,moedas=moedas,ano=ano)
        msg = "Aluno cadastrado com sucesso!" 
    except:
        msg = "Erro ao cadastrar Aluno" 
    
    aluno = Aluno.object.latest('id')
    todos = Aluno.object.all()
    return render(request, 'principal.html', {'aluno':aluno,'todos':todos})

def ano(request):
    return render(request, 'ano.html', {})

def arena(request):
    return render(request, 'arena.html', {})

def principal(request):
    return render(request, 'principal.html', {})
