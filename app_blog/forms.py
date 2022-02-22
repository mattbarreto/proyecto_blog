from django.forms import Form, DateField, ImageField, CharField, URLField, SlugField, BooleanField, ModelForm
from django.db import models
from django.db.models import CASCADE, AutoField, ForeignKey
from ckeditor.fields import RichTextField
from .models import Autor, Categoria

class AvatarFormulario(Form):
    imagen = ImageField(required=True)

class Post_Create(Form):
    id = AutoField(primary_key=True)
    titulo = CharField(max_length=100)
    autor = ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = CharField(max_length=255)
    contenido = RichTextField()
    imagen = URLField(max_length=255)
    slug = SlugField(max_length=100)
    estado = BooleanField()
