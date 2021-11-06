from django import forms
from django.contrib.admin import widgets as wd
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import widgets
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username', 'email', 'first_name', 'last_name', 'telefono')

        labels={
            'username':'Nombre de Usuario',
            'email':'Correo Electronico',
            'first_name':'Nombres',
            'last_name':'Apellidos',
            'telefono':'Telefono'
        }

        widgets={
            'username':wd.AdminTextInputWidget,
            'email':wd.AdminEmailInputWidget,
            'first_name':wd.AdminTextInputWidget,
            'last_name':wd.AdminTextInputWidget,
            'telefono':wd.AdminTextInputWidget
        }
