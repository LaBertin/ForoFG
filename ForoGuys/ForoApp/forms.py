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
    nombre_usuario = forms.CharField(label='Nombre de usuario',
                                     widget=forms.TextInput(attrs={"placeholder":"Ingrese nombre de usuario"}))
    codigo_fallGuy = forms.CharField(label='Codigo FallGuy',
                                     widget=forms.TextInput(attrs={"placeholder":"Codigo FallGuy #"}))
    email = forms.CharField(label='Email',
                                     widget=forms.TextInput(attrs={"placeholder":"Ingrese correo electronico"}))
    contrasena = forms.CharField(label='Contraseña',
                                     widget=forms.TextInput(attrs={"placeholder":"Ingrese contraseña"}))
    repetirContrasena = forms.CharField(label='Confirmar contraseña',
                                     widget=forms.TextInput(attrs={"placeholder":"Ingrese nuevamente contraseña"}))
