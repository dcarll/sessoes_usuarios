from email.policy import HTTP
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

import usuarios
from .models import CustomUsuario
from django.contrib.auth import get_user_model

from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
'''
class CreateUsertoView(CreateView):
	model = CustomUsuario
	form_class = CustomUsuarioCreateForm
	template_name = 'sign_up.html'
	fields = ['nome','preco']
	success_url = reverse_lazy('index')#pra onde vai ser direcionada em caso de sucesso'''

def cadastro(request):
	if request.method == "GET":
		return render(request, 'cadastro.html')
	else:
		username = request.POST.get('usermane')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		senha1 = request.POST.get('senha1')
		senha2 = request.POST.get('senha2')
		senha = senha1 if senha1 == senha2 else messages.error(request, 'Senhas não conferem')


		#recebe user na posição 1, ou seja o usuario que já existe
		user = get_user_model().objects.filter(username=username).first()

		"""se já existir um usuário no banco de dados com esse nome"""
		if user:
			return HttpResponse("Já existe um usuario com esse username")

		user = get_user_model().objects.create(username=email, email=email, password=senha, first_name=first_name, last_name=last_name)
		print(user)
		user.save()

		usuario = get_user_model().objects.filter(username=username).last()
		return HttpResponse(f"Usuario cadastrado com sucesso {usuario}")
		print(get_user_model().get_email_field_name)
		


		return HttpResponse(username)
		

def logar(request):
	if request.method == "GET":
		return render(request, 'login_form.html')
	else:
		username = request.POST.get('email')
		senha = request.POST.get('senha')
		print(f'rmail: {username}')
		print(f'Senha: {senha}')

		user = authenticate(email=username, password=senha)

		if user:
			login(request, user)

			return HttpResponse("Autenticado")
		else:
			return HttpResponse("Email ou senha invalido")

@login_required(login_url='/auth/login/')
def plataforma(request):
		return HttpResponse('Plataforma')
	