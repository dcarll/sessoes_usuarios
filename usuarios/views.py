from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CustomUsuario

from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm

class CreateUsertoView(CreateView):
	model = CustomUsuario
	form_class = CustomUsuarioCreateForm
	template_name = 'sign_up.html'
	fields = ['nome','preco']
	success_url = reverse_lazy('index')#pra onde vai ser direcionada em caso de sucesso