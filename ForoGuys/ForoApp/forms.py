from django import forms
from .models import Post
from .models import Usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class UsuariosFrom(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ('nom_usuario','codigo_fallGuy', 'email', 'contrasena')

class Raw(forms.Form):
    nombre_usuario = forms.CharField()
    codigo_fallGuy = forms.CharField()
    email = forms.CharField()
    contrasena = forms.CharField()
