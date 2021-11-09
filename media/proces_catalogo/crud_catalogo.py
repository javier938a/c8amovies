from django.views.generic import ListView, DetailView
from media.models import CatalogoVideo
from django.shortcuts import redirect, render
from django.http import FileResponse
from django.views.generic import RedirectView

class DetalleCatalogo(DetailView):
	template_name='media/proces_catalogo/detalle_catalogo_video.html'
	model=CatalogoVideo
	context_object_name='detallevideo'
	slug_field='url'
	slug_url_kwarg='url'

	def get_context_data(self, **kwargs):
		context=super(DetalleCatalogo, self).get_context_data(**kwargs)
		slug=self.get_object().get_slug()
		url=self.get_object().get_absolute_url()
		context['slug']=slug
		context['url']=url

		return context


def ver_video(request, pk):
	trailer=CatalogoVideo.objects.get(pk=pk);
	url_video_triller=str(trailer.videotriller)
	#print(url_video_triller)
	return FileResponse(open('/home/javier/Documentos/mis_sistemas/c8amovies/movies/'+url_video_triller, 'rb'))