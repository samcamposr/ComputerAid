from django.db import models
from django.utils import timezone

class Aluno(models.Model):
    object = models.Manager()

    nome=models.CharField(max_length=300)
    senha=models.CharField(max_length=50)
    nick=models.CharField(max_length=50)
    pontuacao=models.IntegerField()
    moedas=models.IntegerField()
    nivel=models.IntegerField()	
    arena=models.CharField(max_length=300)
    ano = models.CharField(max_length=300)