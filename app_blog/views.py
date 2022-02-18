from django.shortcuts import render, redirect, get_object_or_404
from app_blog.forms import AvatarFormulario
from app_blog.models import Avatar, Categoria, Post
from django.db.models import Q

# Create your views here.

def home(request):
    queryset = request.GET.get("buscar")

    post = Post.objects.filter(estado = True)
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()
    
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'index.html', {'avatar_url': avatar_url, 'post': post})

# def detallePost(request,slug):
#     post = get_object_or_404(Post,slug = slug)
#     return render(request, 'post.html', {'detalle_post':post})

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

def blog(request):
    post = Post.objects.all()
    return render(request, 'post.html', {'post': post})

def about(request):
    return render(request, 'about.html')

def contacto(request):
    return render(request, 'contacto.html')

def nutricion(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(
        estado=True, 
        categoria = Categoria.objects.get(nombre__iexact = 'Nutricion')
    )
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True, 
            categoria = Categoria.objects.get(nombre__iexact = 'Nutricion')
        ).distinct()
    return render(request, 'nutricion.html', {'post':post})

def rutinas(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(
        estado=True, 
        categoria=Categoria.objects.get(nombre__iexact='Rutinas')
    )
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True, 
            categoria = Categoria.objects.get(nombre__iexact = 'Rutinas')
        ).distinct()
    
    return render(request, 'rutinas.html', {'post': post})

def saludable(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(
        estado=True, 
        categoria=Categoria.objects.get(nombre__iexact='Saludable')
        )
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True, 
            categoria = Categoria.objects.get(nombre__iexact = 'Saludable')
        ).distinct()
        
    return render(request, 'saludable.html', {'post': post})