from unicodedata import name
from django.urls import path
from .views import agregar_avatar, home, about, contacto, nutricion, rutinas, saludable, leer
from django.contrib.auth.decorators import login_required
from .views import *
urlpatterns = [
    path('user/avatar/add', login_required(agregar_avatar), name='avatar_add'),
    path('', home, name = 'index'),
<<<<<<< HEAD
    path('about', login_required(about), name='about'),
    path('contacto', login_required(contacto), name='contacto'),
    path('nutricion', login_required(nutricion), name='nutricion'),
    path('rutinas', login_required(rutinas), name='rutinas'),
    path('saludable', login_required(saludable), name='saludable'),
    
    path('post/buscar', login_required(post_busqueda), name='Busqueda de Posteos'),
    path('buscar_post', login_required(buscar_post), name='Buscar Posts'),
    
    
=======
    path('leer', leer, name='leer'),
    path('about', about, name='about'),
    path('contacto', contacto, name='contacto'),
    path('nutricion', nutricion, name='nutricion'),
    path('rutinas', rutinas, name='rutinas'),
    path('saludable', saludable, name='saludable'),
>>>>>>> Previo_Funcional
]