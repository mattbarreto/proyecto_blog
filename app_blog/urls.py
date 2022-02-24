from unicodedata import name
from django.urls import path
from .views import agregar_avatar,faq ,home, about, contacto, nutricion, rutinas, saludable, postCreateView, postDeleteView, postUpdateView, autorCreateView, autorListView, autorUpdateView, autorDeleteView, autorDetailView
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('user/avatar/add', login_required(agregar_avatar), name='avatar_add'),
    path('', login_required(home), name='index'),
    path('post/add', login_required(postCreateView.as_view()), name='Crear Post'),
    path('<slug>/update', login_required(postUpdateView.as_view()), name='Actualizar Post'),
    path('<slug>/delete', login_required(postDeleteView.as_view()),name='Borrar Post'),

    path('autor/add', login_required(autorCreateView.as_view()), name='Crear Autor'),
    path('autores', login_required(autorListView.as_view()), name='Autores'),
    path('autor/detail/<pk>', login_required(autorDetailView.as_view()), name='Datos del Autor'),
    path('autor/update/<pk>', login_required(autorUpdateView.as_view()),name='Actualizar Autor'),
    path('autor/delete/<pk>', login_required(autorDeleteView.as_view()), name='Borrar Autor'),

    path('about', login_required(about), name='about'),
    path('contacto', login_required(contacto), name='contacto'),
    path('nutricion', login_required(nutricion), name='nutricion'),
    path('rutinas', login_required(rutinas), name='rutinas'),
    path('saludable', login_required(saludable), name='saludable'),
    path('faq', login_required(faq), name='faq'),
    
    path('post/buscar', login_required(post_busqueda), name='Busqueda de Posteos'),
    path('buscar_post', login_required(buscar_post), name='Buscar Posts'),
]