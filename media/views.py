from django.shortcuts import render

from django.views.generic import TemplateView
from media.proces_usuario.crud_usuario import RegistrarUsuario
from media.proces_usuario.crud_usuario import Login, Logout
from media.proces_catalogo.crud_catalogo import DetalleCatalogo, ver_video
#obteniendo el modelo de catalogo
from .models import CatalogoVideo

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
        catalogos=CatalogoVideo.objects.all()

        page=self.request.GET.get('page',1)

        datos=self.paginar_catalogos(catalogos, page)
        context['paginator']=datos['paginator']
        context['entity']=datos['cata']
        
        return context