from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail,name='detalle_publicacion'),
    url(r'^post/new/$', views.post_new, name='nuevo_post'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='editar'),
    url(r'^inicio', views.inicio, name= 'Inicio' ),
    url(r'^iniciasesion', views.iniciasesion, name= 'iniciasesion' ),
    url(r'^registrarse', views.registrarse, name= 'registrarse' ),
    url(r'^top_jugadores', views.top_jugadores, name= 'top_jugadores' ),
    url(r'^trucasos', views.trucasos, name= 'trucasos' ),

]
