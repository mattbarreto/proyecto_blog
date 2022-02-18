from django.shortcuts import render, redirect
from app_blog.forms import AvatarFormulario
from app_blog.models import Avatar, Categoria, Post

# Create your views here.

def home(request):

    post = Post.objects.filter(estado = True)
    
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'index.html', {'avatar_url': avatar_url, 'post': post})

# Avatar
def agregar_avatar(request):
    if request.method == 'POST':
        formulario = AvatarFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            avatar = Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return redirect('index')
    else:   
        formulario = AvatarFormulario()
        
    return render(request, 'crear_avatar.html', {'form': formulario})

def nutricion(request):
    post = Post.objects.filter(
        estado=True, 
        categoria=Categoria.objects.get(nombre__iexact='Nutricion')
    )
    return render(request, 'nutricion.html', {'post':post})

def rutinas(request):
    post = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre__iexact='Rutinas'))
    return render(request, 'rutinas.html', {'post': post})

def saludable(request):
    post = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre__iexact='Saludable'))
    return render(request, 'saludable.html', {'post': post})

def leer(request, post):
    return render(request, 'post.html', {'post': Post.objects.all()})

def about(request):
    return render(request, 'about.html')

def contacto(request):
    return render(request, 'contact.html')
