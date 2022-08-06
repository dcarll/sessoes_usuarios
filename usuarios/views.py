from email.policy import HTTP
from django.http import HttpResponse


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
		email = request.POST.get('email')
		senha = request.POST.get('senha')

		#recebe user na posição 1, ou seja o usuario que já existe
		user = get_user_model().objects.filter(username=username).first()

		"""se já existir um usuário no banco de dados com esse nome"""
		if user:
			return HttpResponse("Já exixte um usuario com esse username")
		user = get_user_model().objects.create(username=username, email=email, password=senha)
		user.save()

		usuario = get_user_model().objects.filter(username=username).last()
		return HttpResponse(f"Usuario cadastrado com sucesso {usuario}")
		print(get_user_model().get_email_field_name)
		


		return HttpResponse(username)
		

def login(request):
	return render(request, 'login.html')