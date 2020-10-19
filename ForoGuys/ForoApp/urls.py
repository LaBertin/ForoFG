from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail,name='detalle_publicacion'),
    url(r'^post/new/$', views.post_new, name='nuevo_post'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='editar'),
]
