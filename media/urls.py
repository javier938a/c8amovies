from django.urls import path, include

#importando la vista principal
from .views import Principal
from .views import RegistrarUsuario, Login, Logout


app_name='video'
urlpatterns=[
    path('index/', Principal.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registrar_usuario/', RegistrarUsuario.as_view(), name='registrar')

]