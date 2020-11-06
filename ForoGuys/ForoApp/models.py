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
