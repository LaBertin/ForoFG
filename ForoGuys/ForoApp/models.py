from django.db import models
from django.utils import timezone

class Post(models.Model):
    Autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Código_FallGuys = models.CharField(max_length=4)
    Título = models.CharField(max_length=200)
    Texto = models.TextField(max_length=500)
    Fecha_Creación = models.DateTimeField(
        default=timezone.now)
    Fecha_Publicación = models.DateTimeField(
        blank=True, null=True)
def publish(self):
    self.Fecha_Publicación = timezone.now()
    self.save()

def __str__(self):
    return self.title