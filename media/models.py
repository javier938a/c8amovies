from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.

class UserManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(username=username)

class User(AbstractUser):
    objects=UserManager()
    fecha_nacimiento=models.DateField(null=True, blank=True)
    telefono=models.CharField(help_text='Ingrese su numero de Telefono', max_length=8, null=True)
    
    class Meta:
        db_table='auth_user'
    
    def natural_key(self):
        return self.username


class CategoriaCatalogo(models.Model):
    categoria=models.CharField(help_text='Ingrese la categoria de la pelicula, serie o video, como niños, adultos, etc', max_length=100)
    
    def __str__(self):
        return self.categoria

class ClasificacionCatalogo(models.Model):
    clasificacion=models.CharField(max_length=10, help_text='Ingrese la clasificacion de la pelicula serie o novela, como A, B, C')
    
    def __str__(self):
        return self.clasificacion


class TipoCatalog(models.Model):
    tipo=models.CharField(max_length=20, help_text='Ingrese el tipo de catalogo como novela, serie, pelicula')

    def __str__(self):
        return self.tipo

class CatalogoVideo(models.Model):
    catalog_nombre=models.CharField(help_text='Ingrese el nombre de la serie novela o pelicula', max_length=100)
    sipnosis=models.TextField(help_text='Ingrese la sipnosis de la novela o serie o pelicula')
    author=models.CharField(help_text='Ingrese el nombre del autor', max_length=50)
    nocap=models.IntegerField(help_text='Ingrese la cantidad de capitulos que tiene la pelicula o o serie')
    img_presentacion=models.ImageField(upload_to='img_pre')
    idcategoria=models.ForeignKey(CategoriaCatalogo, on_delete=models.CASCADE, help_text='Ingrese el tipo de catalogo')
    idclasificacion=models.ForeignKey(ClasificacionCatalogo, on_delete=models.CASCADE, help_text='Ingrese la clasificacion, del video')
    idtipo=models.ForeignKey(TipoCatalog, on_delete=models.CASCADE, help_text='Ingrese el tipo de video')
    anio_lanza=models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return "%s, %s"%(self.catalog_nombre, self.sipnosis)


class Videos(models.Model):
    cap=models.CharField(help_text="Ingrese el numero de capitulo", max_length=50)
    idcatalog=models.ForeignKey(CatalogoVideo ,help_text="Ingrese el catalogo al que pertenece el video", on_delete=models.CASCADE)
    video=models.FileField(upload_to='videos')
    miniatura=models.ImageField(upload_to="mini_img_video")

    def __str__(self):
        return "cap %s"%self.cap

class Visualizaciones(models.Model):
    idusuario=models.ForeignKey(User, on_delete=models.CASCADE, help_text="Ingrese el id del usuario")
    video=models.ForeignKey(Videos, on_delete=models.CASCADE, help_text='Ingrese el Video a visualizar')
    hora=models.CharField(max_length=4, help_text="Ingrese la hora en que termino de ver el video", null=True, blank=True)
    minuto=models.CharField(max_length=4, help_text='Ingrese el minuto en que dejo de ver el video', null=True, blank=True)
    segundo=models.CharField(max_length=4, help_text='Ingrese el segundo en que se quedo el video', null=True, blank=True)
    fecha_visualizacion=models.DateField(auto_now_add=True, help_text='Ingrese la fecha de visualizacion')

    def __str__(self):
        return "visualizacion %s %s"%(self.video, self.idusuario)