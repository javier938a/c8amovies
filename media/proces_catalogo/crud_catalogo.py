from django.views.generic import ListView, DetailView
from media.models import CatalogoVideo
from django.shortcuts import redirect, render
from django.http import FileResponse
from django.views.generic import RedirectView
from io import BytesIO
import urllib
import urllib.parse
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


#https://uc94059b7b2587173e617d95ab0a.dl.dropboxusercontent.com/cd/0/get/BZrlx2ZsBTX-5zes9wuq4aISxoyzBuF2ZiwFHhJEONraPFGBs_bSSwdEMsdzUfI-_nI1lJ2txkpKJ_q-b29NHYyPpRj2pC1BwG8la84Lc20oJdM1UxIEi2G6hl8BxdrkKeinpgdsS7r8L0-24L6hT0Nu/file
def ver_video(request, pk):
	trailer=CatalogoVideo.objects.get(pk=pk);
	#print(link)
	bytes_video=''
	with urllib.request.urlopen(trailer.videotriller.url) as bytesvideo:
		bytes_video=bytesvideo.read()
	
	
	datos_videos=BytesIO(bytes_video)

	print(bytes_video)
	return FileResponse(datos_videos, content_type='video/mp4')