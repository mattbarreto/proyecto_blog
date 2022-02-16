from django.urls import path
from .views import home, about, contacto, nutricion, rutinas, saludable

urlpatterns = [
    path('', home, name = 'index'),
    path('', about, name='about'),
    path('', contacto, name='contacto'),
    path('', nutricion, name='nutricion'),
    path('', rutinas, name='rutinas'),
    path('', saludable, name='saludable'),
]
