from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('user/avatar/add', agregar_avatar, name='avatar_add'),
    path('', home, name = 'index'),
    path('about', about, name='about'),
    path('contacto', contacto, name='contacto'),
    path('nutricion', nutricion, name='nutricion'),
    path('rutinas', rutinas, name='rutinas'),
    path('saludable', saludable, name='saludable'), 
    path('blog/all', blog, name='blog'),
]