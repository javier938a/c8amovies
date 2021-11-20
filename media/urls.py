from django.urls import path, include

#importando la vista principal
from .views import Principal
from .views import RegistrarUsuario, Login, Logout
from .views import DetalleCatalogo, ver_video, ver_image_video, ver_image_catalogo
from .views import VideoCap, ver_video_cap, guardar_visualizaciones



app_name='video'
urlpatterns=[
    path('index/', Principal.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registrar_usuario/', RegistrarUsuario.as_view(), name='registrar'),
    path('detallecatalogo/<slug:url>/<int:pk>', DetalleCatalogo.as_view(), name='detallecatalog'),
    path('ver-video/<int:pk>', ver_video, name='view_video'),
    path('ver-image-video/<int:pk>', ver_image_video, name='view_img_video'),
    path('ver-image-catalogo/<int:pk>', ver_image_catalogo, name='view_img_catalog'),
    path('capitulo/<int:pk>', VideoCap.as_view(), name='view_video_cap'),
    path('ver-video-cap/<int:pk>', ver_video_cap, name='view_cap'),
    path('guardar_visualizaciones/', guardar_visualizaciones, name='save_video_view')
]