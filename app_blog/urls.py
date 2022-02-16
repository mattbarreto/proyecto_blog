from django.urls import path
from .views import agregar_avatar, home

urlpatterns = [
    path('', home, name = 'index'),
    path('user/avatar/add', agregar_avatar, name='avatar_add'),
]
