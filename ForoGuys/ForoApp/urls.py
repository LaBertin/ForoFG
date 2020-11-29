from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib import admin
from django.urls import path, re_path, include
from django.urls import reverse_lazy


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
    url(r'^usuarios', views.usuarios, name= 'usuarios' ),
    url(r'^listar', views.user_list, name='listar'),
    url(r'^password_reset_form', views.password_reset_form, name= 'password_reset_form' ),
    url(r'^password_reset_done', views.password_reset_done, name= 'password_reset_done' ),
    url(r'^password_reset_email', views.password_reset_email, name= 'password_reset_email' ),
    url(r'^password_reset_confirm', views.password_reset_confirm, name= 'password_reset_confirm' ),
    url(r'^password_reset_complete', views.password_reset_complete, name= 'password_reset_complete' ),
    path('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_forms.html', email_template_name="registration/password_reset_email.html"), name = 'password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name = 'password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirms.html'), name = 'password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html') , name = 'password_reset_complete'),
]
