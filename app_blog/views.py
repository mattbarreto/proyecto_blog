from django.shortcuts import render, redirect, get_object_or_404
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

def detallePost(request,slug):
    post = Post.objects.get(
        slug = slug
    )
    print(post)
    return render(request, 'post.html')

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

# def category(request, categoy_id):
#     category = get_object_or_404(Categoria, id=categoy_id)
#     return render(request, 'categoria.html', {'category': category})

def about(request):
    return render(request, 'about.html')

def contacto(request):
    return render(request, 'contact.html')

def nutricion(request):
    post = Post.objects.filter(
        estado=True, 
        categoria = Categoria.objects.get(nombre = 'Nutricion')
    )
    return render(request, 'nutricion.html', {'post':post})

def rutinas(request):
    post = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre='Rutinas'))
    return render(request, 'rutinas.html', {'post': post})

def saludable(request):
    post = Post.objects.filter(estado=True, categoria=Categoria.objects.get(nombre='Saludable'))
    return render(request, 'saludable.html', {'post': post})


