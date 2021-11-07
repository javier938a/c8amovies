from django.contrib import admin
from .models import User
from .models import CategoriaCatalogo, ClasificacionCatalogo, TipoCatalog, CatalogoVideo
from .models import Videos, Visualizaciones

# Register your models here.
admin.site.register(User)
admin.site.register(CategoriaCatalogo)
admin.site.register(ClasificacionCatalogo)
admin.site.register(TipoCatalog)
admin.site.register(CatalogoVideo)
admin.site.register(Videos)
admin.site.register(Visualizaciones)