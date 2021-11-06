from django.db import models
from django.views.generic import CreateView, ListView, DetailView
from media.models import User
from media.forms import UserForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView


class RegistrarUsuario(CreateView):
    template_name='media/proces_usuario/registrar_usuario.html'
    models=User
    form_class=UserForm
    context_object_name='form'
    success_url=reverse_lazy('video:index')

class Login(LoginView):
    template_name='media/proces_usuario/login.html'
    contex_object_name='form'
  

    def get_success_url(self):
        return reverse_lazy('video:index')

class Logout(LogoutView):
    template_name='media/proces_usuario/logout.html'





