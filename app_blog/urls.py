from django.urls import path
from .views import agregar_avatar, blog, home, about, contacto, nutricion, rutinas, saludable

urlpatterns = [
    path('user/avatar/add', agregar_avatar, name='avatar_add'),
    path('', home, name = 'index'),
    path('blog', blog, name='blog'),
    path('about', about, name='about'),
    path('contacto', contacto, name='contacto'),
    path('nutricion', nutricion, name='nutricion'),
    path('rutinas', rutinas, name='rutinas'),
    path('saludable', saludable, name='saludable'),
]