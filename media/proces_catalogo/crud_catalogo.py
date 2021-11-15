from django.views.generic import ListView, DetailView
from media.models import CatalogoVideo, Videos, TemporadaVideo
from django.shortcuts import redirect, render
from django.http import FileResponse
from django.views.generic import RedirectView
from django.shortcuts import redirect

class DetalleCatalogo(DetailView):
	template_name='media/proces_catalogo/detalle_catalogo_video.html'
	model=CatalogoVideo
	context_object_name='detalleCatalogVideo'
	slug_field='url'
	slug_url_kwarg='url'

	def get_context_data(self, **kwargs):
		context=super(DetalleCatalogo, self).get_context_data(**kwargs)
		slug=self.get_object().get_slug()
		url=self.get_object().get_absolute_url()
		context['slug']=slug
		context['url']=url

		#obtener todas las temporadas
		videos_x_temporada={}
		video_catalogo=Videos.objects.filter(idcatalog=self.get_object().pk)

		temporadas=TemporadaVideo.objects.all()
		i=0
		for temp in temporadas:
			i=i+1
			#verificando si existen video para cad auna de las temporadas de lo contario no muestra
			if(video_catalogo.filter(idtemporada__pk=temp.pk).exists()):
				videos_x_temporada[(str(i))]=video_catalogo.filter(idtemporada__pk=temp.pk)




		context['temporadas']=videos_x_temporada

		return context


def ver_video(request, pk):
	trailer=CatalogoVideo.objects.get(pk=pk)
	return redirect(trailer.videotriller.url)

def ver_image_video(request, pk):
	image_video=Videos.objects.get(pk=pk)

	return redirect(image_video.miniatura.url)

def ver_image_catalogo(reques, pk):
	image_video_catalog=CatalogoVideo.objects.get(pk=pk)
	return redirect(image_video_catalog.img_presentacion.url)


