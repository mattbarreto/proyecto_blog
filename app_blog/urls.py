from django.urls import path
from .views import agregar_avatar, home
from .views import home, about, contacto, nutricion, rutinas, saludable

urlpatterns = [
    path('', home, name = 'index'),
    path('user/avatar/add', agregar_avatar, name='avatar_add'),
    path('', home, name = 'index'),
    path('', about, name='about'),
    path('', contacto, name='contacto'),
    path('', nutricion, name='nutricion'),
    path('', rutinas, name='rutinas'),
    path('', saludable, name='saludable'),
]
