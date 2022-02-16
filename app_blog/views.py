from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

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