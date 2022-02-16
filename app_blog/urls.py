from django.urls import path
<<<<<<< HEAD
from .views import agregar_avatar, home

urlpatterns = [
    path('', home, name = 'index'),
    path('user/avatar/add', agregar_avatar, name='avatar_add'),
=======
from .views import home, about, contacto, nutricion, rutinas, saludable

urlpatterns = [
    path('', home, name = 'index'),
    path('', about, name='about'),
    path('', contacto, name='contacto'),
    path('', nutricion, name='nutricion'),
    path('', rutinas, name='rutinas'),
    path('', saludable, name='saludable'),
>>>>>>> 9871151feb3b769735fcf070f2bcc50e8767c010
]
