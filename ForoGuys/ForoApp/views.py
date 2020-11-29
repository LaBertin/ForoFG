from django.shortcuts import render
from .models import Post
from .models import Usuarios, Noticia, Trucos, mostrarusuario
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import UsuariosFrom, Raw, CustomUserCreateForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model




def password_reset_form(request):
    data= {
        'form':Raw()
    }
    return render(request,'recuperarcontraseña/password_reset_form.html',data)

def password_reset_done(request):
    return render(request,'recuperarcontraseña/password_reset_done.html')

def password_reset_email(request):
    return render(request,'recuperarcontraseña/password_reset_email.html')

def password_reset_confirm(request):
    return render(request,'recuperarcontraseña/password_reset_confirm.html')

def password_reset_complete(request):
    return render(request,'recuperarcontraseña/password_reset_complete.html')

def usuarios(request):
    user = User.objects.all
    context = {'usuarios':user}
    return render(request,'Usuarios/usuarios.html', context)


def registro(request):
    data= {
        'form':CustomUserCreateForm()
    }

    if request.method=='POST':
        formulario =CustomUserCreateForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()


            return redirect(to="/")
        data["form"]=formulario
    return render(request,'registration/registro.html',data)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'ForoApp/detalle_publicacion.html', {'post': post})

def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('detalle_publicacion', pk=post.pk)

        else:
            form = PostForm()
        return render(request, 'ForoApp/editar.html', {'form': form})

def user_list(request):
    usuario = User.objects.all()
    context = {'usuarios':usuario}
    return render(request, 'Usuarios/usuarios.html', context)

def user_remove(request,id):
    usuario = User.objects.all()
    usuario.delete()

    return redirect ('usuarios')

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detalle_publicacion', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'ForoApp/editar.html', {'form': form})



def inicio(request):
    noti = Noticia.objects.all();
    context = {'noticias':noti}
    return render(request,'ForoApp/inicio.html',context)

def iniciasesion(request):
    return render(request,'ForoApp/iniciasesion.html')



def trucasos(request):
    truco = Trucos.objects.all();
    context = {'trucasos':truco}
    return render(request,'ForoApp/trucasos.html' , context)

def top_jugadores(request):
    return render(request,'ForoApp/top_jugadores.html')

def juntas(request):
    return render(request,'ForoApp/juntas.html')


def foro(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'ForoApp/foro.html', {'posts': posts})
