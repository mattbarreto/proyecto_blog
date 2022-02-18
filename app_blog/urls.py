from django.urls import path
from .views import agregar_avatar, home, about, contacto, nutricion, rutinas, saludable, leer
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('user/avatar/add', login_required(agregar_avatar), name='avatar_add'),
    path('', home, name = 'index'),
    path('leer', leer, name='leer'),
    path('about', about, name='about'),
    path('contacto', contacto, name='contacto'),
    path('nutricion', nutricion, name='nutricion'),
    path('rutinas', rutinas, name='rutinas'),
    path('saludable', saludable, name='saludable'),
]