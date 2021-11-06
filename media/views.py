from django.shortcuts import render

from django.views.generic import TemplateView
from media.proces_usuario.crud_usuario import RegistrarUsuario
from media.proces_usuario.crud_usuario import Login, Logout


# Create your views here.

class Principal(TemplateView):
    template_name='media/index.html'