from django.urls import path
from .views import CreateUsertoView

urlpatterns = [
	path('juntar/', CreateUsertoView.as_view(), name='juntar'),
]