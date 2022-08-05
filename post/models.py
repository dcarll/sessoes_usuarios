from django.contrib.auth.models import User
#from django.conf import Settings
from django.contrib.auth import get_user_model
#importa u modelo de usuario que está sendo usado

from django.db import models


class Base(models.Model):
	data_criacao = models.DateField('Criação', auto_now_add=True) 
	data_publicacao = models.DateField('Publicacao', auto_now=True)

# Create your models here.
class Postagem(Base):
	titulo = models.CharField(max_length=255)
	conteudo = models.TextField()
	autor = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE, default=None)