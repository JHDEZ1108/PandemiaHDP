from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CommentForm
from .models import Comment, Blog


# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)  # Cookie Django
                return redirect('blog')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El Username ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('blog')

def create_comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # Obtiene el blog o devuelve un error 404 si no existe
    if request.method == 'GET':
        return render(request, 'create_comment.html', {
            'form': CommentForm(),
            'blog': blog  # Pasar el blog al contexto puede ser útil para mostrar información en la plantilla
        })
    else:
        try:
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.user = request.user
                new_comment.blog = blog  # Asocia el comentario con el blog
                new_comment.save()
                return redirect('blog_detail', blog_id=blog.id)  # Redirige a la vista detallada del blog
        except ValueError:
            return render(request, 'create_comment.html', {
                'form': CommentForm(),
                'error': 'Error al agregar comentario',
                'blog': blog
            })

def blog(request):
    blogs = Blog.objects.all()  # Obtiene todos los blogs
    return render(request, 'blog.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = blog.comments.all()  # Utiliza el related_name para obtener todos los comentarios asociados
    return render(request, 'blog_detail.html', {'blog': blog, 'comments': comments})
