from django.urls import path, include

#importando la vista principal
from .views import Principal
from .views import RegistrarUsuario, Login, Logout
from .views import DetalleCatalogo, ver_video, ver_image_video, ver_image_catalogo



app_name='video'
urlpatterns=[
    path('index/', Principal.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registrar_usuario/', RegistrarUsuario.as_view(), name='registrar'),
    path('detallecatalogo/<slug:url>/<int:pk>', DetalleCatalogo.as_view(), name='detallecatalog'),
    path('ver_video/<int:pk>', ver_video, name='view_video'),
    path('ver_image_video/<int:pk>', ver_image_video, name='view_img_video'),
    path('ver_image_catalogo/<int:pk>', ver_image_catalogo, name='view_img_catalog')
]