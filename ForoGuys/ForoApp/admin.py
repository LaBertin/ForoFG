from django.contrib import admin
from .models import Post
from .models import Usuarios, Noticia, Trucos

admin.site.register(Post)
admin.site.register(Usuarios)
admin.site.register(Noticia)
admin.site.register(Trucos)
