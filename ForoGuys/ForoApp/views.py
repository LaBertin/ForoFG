from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
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
    return render(request,'ForoApp/inicio.html')

def iniciasesion(request):
    return render(request,'ForoApp/iniciasesion.html')

def registrarse(request):
    return render(request,'ForoApp/registrarse.html')

def trucasos(request):
    return render(request,'ForoApp/trucasos.html')

def top_jugadores(request):
    return render(request,'ForoApp/top_jugadores.html')

def foro(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'ForoApp/foro.html', {'posts': posts})
