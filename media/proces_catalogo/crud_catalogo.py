from django.views.generic import ListView, DetailView
from media.models import CatalogoVideo

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