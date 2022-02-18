from django.urls import path
<<<<<<< HEAD
from .views import agregar_avatar, home, about, contacto, nutricion, rutinas, saludable, leer
=======
from .views import agregar_avatar, home, about, contacto, nutricion, rutinas, saludable
from django.contrib.auth.decorators import login_required
>>>>>>> origin/Previo_Funcional_Luca

urlpatterns = [
    path('user/avatar/add', login_required(agregar_avatar), name='avatar_add'),
    path('', home, name = 'index'),
<<<<<<< HEAD
    path('leer', leer, name='leer'),
    path('about', about, name='about'),
    path('contacto', contacto, name='contacto'),
    path('nutricion', nutricion, name='nutricion'),
    path('rutinas', rutinas, name='rutinas'),
    path('saludable', saludable, name='saludable'),
=======
    path('about', login_required(about), name='about'),
    path('contacto', login_required(contacto), name='contacto'),
    path('nutricion', login_required(nutricion), name='nutricion'),
    path('rutinas', login_required(rutinas), name='rutinas'),
    path('saludable', login_required(saludable), name='saludable'),
>>>>>>> origin/Previo_Funcional_Luca
]