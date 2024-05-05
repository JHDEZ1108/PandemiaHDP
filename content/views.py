from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages  # Importa esto para enviar mensajes al template
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CommentForm, BlogForm, SignUpForm
from .models import Comment, Blog



# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': SignUpForm()})
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('blog')  # Asegúrate de que 'blog' es el nombre correcto de la URL de redirección deseada
            except IntegrityError as e:
                # Aquí puedes comprobar si el error es específico de un nombre de usuario duplicado o algo más
                error_message = 'El nombre de usuario ya está en uso' if 'UNIQUE constraint' in str(e) else 'Ocurrió un error al crear el usuario'
                return render(request, 'signup.html', {'form': SignUpForm(), 'error': error_message})
        else:
            # En caso de que el formulario no sea válido, se renderiza de nuevo con los errores.
            return render(request, 'signup.html', {'form': form, 'error': form.errors})

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

@login_required
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


def es_superusuario(user):
    return user.is_superuser

@login_required
@user_passes_test(es_superusuario)
def create_or_update_blog(request, blog_id=None):
    template_name = 'create_blog.html'  # Plantilla predeterminada para crear un nuevo blog
    
    blog = None
    if blog_id:
        blog = get_object_or_404(Blog, pk=blog_id, user=request.user)  # Asegura que solo el autor pueda editar
        template_name = 'update_blog.html'  # Cambia la plantilla para actualizar un blog existente
    
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        try:
            if form.is_valid():
                saved_blog = form.save(commit=False)
                if not blog_id:  # Solo establece el usuario si es un nuevo blog
                    saved_blog.user = request.user
                saved_blog.save()
                return redirect('blog_detail', blog_id=saved_blog.id)
        except ValueError as e:
            # Maneja el error específico aquí. Por ejemplo, podrías enviar un mensaje al template.
            messages.error(request, f'Error al guardar el blog: {e}')
    else:
        form = BlogForm(instance=blog)

    return render(request, template_name, {
        'form': form,
        'blog': blog  # Pasar el blog al contexto puede ser útil
    })
def hipertension(request):
    return render(request, 'hipertension.html')
def colesterol(request):
    return render(request, 'colesterol.html')
def artritis(request):
    return render(request, 'artritis.html')
def renal(request):
    return render(request, 'renal.html')
def cardiaca(request):
    return render(request, 'cardiaca.html')
def alzheimer(request):
    return render(request, 'alzheimer.html')
def cancer(request):
    return render(request, 'cancer.html')
def asma(request):
    return render(request, 'asma.html')
def diabetes(request):
    return render(request, 'diabetes.html')
def vih(request):
    return render(request, 'vih.html')
def EPOC(request):
    return render(request, 'EPOC.html')
def epilepsia(request):
    return render(request, 'epilepsia.html')