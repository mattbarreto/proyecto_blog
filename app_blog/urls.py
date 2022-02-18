from django.urls import path
from .views import agregar_avatar, home, about, contacto, nutricion, rutinas, saludable
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('user/avatar/add', login_required(agregar_avatar), name='avatar_add'),
    path('', home, name = 'index'),
    path('about', login_required(about), name='about'),
    path('contacto', login_required(contacto), name='contacto'),
    path('nutricion', login_required(nutricion), name='nutricion'),
    path('rutinas', login_required(rutinas), name='rutinas'),
    path('saludable', login_required(saludable), name='saludable'),
]