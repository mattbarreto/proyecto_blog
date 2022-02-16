from django.shortcuts import render, redirect
from app_blog.forms import AvatarFormulario
from app_blog.models import Avatar


# Create your views here.

def home(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'index.html', {'avatar_url': avatar_url})



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


def about(request):
    return render(request, 'about.html')

def contacto(request):
    return render(request, 'contact.html')

def nutricion(request):
    return render(request, 'nutricion.html')

def rutinas(request):
    return render(request, 'rutinas.html')

def saludable(request):
    return render(request, 'saludable.html')
