from django.db import models


class Base(models.Model):
	data_criacao = models.DateField('Criação', auto_now_add=True) 

# Create your models here.
class Postagem(models.Model):
	titulo = models.CharField(max_length=255)
	conteudo = models.TextField()