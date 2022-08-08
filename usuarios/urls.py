from django.urls import path, include
from . import views
# from django.contrib.auth import views as auth_views



urlpatterns = [
	# path('cadastro/', views.cadastro, name='cadastro'),
	# path('login/', auth_views.LoginView.as_view(
	# 	template_name='login_form.html'), name='login'),
	# path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('plataforma/', views.plataforma, name='plataforma'),
	# path('auth/', include('allauth.urls')),
]