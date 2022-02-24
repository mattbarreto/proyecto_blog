from dataclasses import fields
from django.forms import Form, DateField, ImageField, CharField, URLField, SlugField, BooleanField
from django.db import models
from django.db.models import CASCADE, AutoField, ForeignKey
from ckeditor.fields import RichTextField
from .models import Autor, Categoria, Post

class AvatarFormulario(Form):
    imagen = ImageField(required=True)

class Post_Create(Form):
    class Meta:
        model = Post
        fields = ('__all__')

class Autor_Create(Form):
    class Meta:
        model = Autor
        fields = ('__all__')
