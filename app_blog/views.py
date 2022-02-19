from http.client import HTTPResponse
from django.shortcuts import render, redirect
from app_blog.forms import AvatarFormulario
from app_blog.models import Avatar, Categoria, Post
from django.db.models import Q
# Create your views here.

# def home(request):
#     queryset = request.GET.get("buscar")
#     post = Post.objects.filter(estado = True)
#     if queryset:
#         post = Post.objects.filter(
#             Q(titulo__icontains = queryset) |
#             Q(descripcion__icontains = queryset)
#         ).distinct()
    
#     avatares = Avatar.objects.filter(user=request.user.id)
#     if avatares:
#         avatar_url = avatares.last().imagen.url
#     else:
#         avatar_url = ''
#     return render(request, 'index.html', {'avatar_url': avatar_url, 'post': post})



def home(request):
    post = Post.objects.filter(estado = True)
    queryset = request.GET.get("buscar")
    
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(slug__icontains=queryset)
        ).distinct()
        return render(request, "posteos.html", {"poste": post, "query": queryset})
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
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'nutricion.html', {'avatar_url': avatar_url,'post':post})

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
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'rutinas.html', {'avatar_url': avatar_url,'post': post})

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
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''  
    return render(request, 'saludable.html', {'avatar_url': avatar_url,'post': post})

def leer(request, titulo):
    post = Post.objets.get(titulo = titulo)
    return render(request, 'post.html', {'leer': post})

def about(request):
    return render(request, 'about.html')

def contacto(request):
    return render(request, 'contact.html')

def post_busqueda(request):

    return render(request, 'rutinas_busqueda.html')

def buscar_post(request):
    if request.GET["pos"]:
        posteo = request.GET["pos"]
        poste = Post.objects.filter(titulo__icontains=posteo)
        return render(request, "post.html", {"poste": poste, "query": posteo})
    else:
        mensaje = "Por favor, introduzca un nombre para comenzar la búsqueda"
    return HTTPResponse(mensaje)
    