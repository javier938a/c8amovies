from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.

class UserManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(username=username)

class User(AbstractUser):
    objects=UserManager()
    fecha_nacimiento=models.DateField(null=True, blank=True)
    telefono=models.CharField(help_text='Ingrese su numero de Telefono', max_length=8, null=True)
    
    class Meta:
        db_table='auth_user'
    
    def natural_key(self):
        return self.username

class Videos(models.Model):
    pass
