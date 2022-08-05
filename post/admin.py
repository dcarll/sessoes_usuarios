from atexit import register
from django.contrib import admin
from .models import Postagem

# Register your models here.

@register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao', 'data_publicacao')
