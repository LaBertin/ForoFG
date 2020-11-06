from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Código_FallGuys = models.CharField(max_length=4)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    def publish(self):
        self.Fecha_Publicación = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Usuarios(models.Model):
    nom_usuario = models.CharField(max_length=25)
    codigo_fallGuy = models.CharField(max_length=4)
    email = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=25)

class Trucos(models.Model):
    mapa = models.CharField(max_length=60)
    imagen_truco = models.ImageField(upload_to="Trucos", null=True)
    desc_truco = models.CharField(max_length=600)
    def __str__(self):
        return self.mapa

class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    desc = models.CharField(max_length=600)
    fecha = models.DateTimeField(
        default=timezone.now)
    imagen = models.ImageField(upload_to="Noticia", null=True)

    def __str__(self):
        return self.titulo

class mostrarusuario(models.Model):
    username=models.CharField(max_length=100)
