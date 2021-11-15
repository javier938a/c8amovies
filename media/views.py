from django.shortcuts import render

from django.views.generic import TemplateView
from media.proces_usuario.crud_usuario import RegistrarUsuario
from media.proces_usuario.crud_usuario import Login, Logout
from media.proces_catalogo.crud_catalogo import DetalleCatalogo, ver_video, ver_image_video, ver_image_catalogo
from media.proces_video.crud_video import VideoCap, ver_video_cap
#obteniendo el modelo de catalogo
from .models import CatalogoVideo, CategoriaCatalogo

from django.http import Http404

from django.core.paginator import Paginator


# Create your views here.

class Principal(TemplateView):
    template_name='media/index.html'

    def paginar_catalogos(self, catalogos, page):
        cata=None
        paginator=None
        datos={}
        try:
            paginator=Paginator(catalogos, 20)
            cata=paginator.page(page)
            datos['paginator']=paginator
            datos['cata']=cata
        except:
            raise Http404
        return datos

    def get_context_data(self, **kwargs):
        context=super(Principal, self).get_context_data(**kwargs)

        categorias=CategoriaCatalogo.objects.all()

        catalogos_x_categorias={}
        catalog=CatalogoVideo.objects.all()
        for cate in categorias:
            catalogos=CatalogoVideo.objects.filter(idcategoria__id=cate.pk)
            catalogos_x_categorias[cate.categoria]=catalogos

        context['catalog_cate']=catalogos_x_categorias
        
        return context