from media.models import Videos
from django.views.generic import DetailView

from media.models import Videos, TemporadaVideo, CatalogoVideo

from django.shortcuts import redirect

class VideoCap(DetailView):
	template_name='media/proces_video/detalleVideo.html'
	model=Videos
	context_object_name='detalleVideo'

	def get_context_data(self, **kwargs):
		context=super(VideoCap, self).get_context_data(**kwargs)
		#obtener todas las temporadas

		videos_x_temporada={}
		video_catalogo=Videos.objects.filter(idcatalog=self.get_object().idcatalog.pk)

		temporadas=TemporadaVideo.objects.all()
		i=0
		for temp in temporadas:
			i=i+1
			if video_catalogo.filter(idtemporada__pk=temp.pk).exists():
				videos_x_temporada[(str(i))]=video_catalogo.filter(idtemporada__pk=temp.pk)




		context['temporadas']=videos_x_temporada

		return context

def ver_video_cap(request, pk):
	video_cap_select=Videos.objects.get(pk=pk)

	return redirect(video_cap_select.video.url)




	