from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail,name='detalle_publicacion'),
    url(r'^post/new/$', views.post_new, name='nuevo_post'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='editar'),
    url(r'^$', views.inicio, name= 'Inicio' ),
    url(r'^iniciasesion', views.iniciasesion, name= 'iniciasesion' ),

    url(r'^top_jugadores', views.top_jugadores, name= 'top_jugadores' ),
    url(r'^trucasos', views.trucasos, name= 'trucasos' ),
    url(r'^foro', views.foro, name= 'foro' ),
    url(r'^registro', views.registro, name='registro'),
]
