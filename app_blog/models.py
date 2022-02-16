from pickle import FALSE
from tkinter.tix import Tree
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from tkinter import CASCADE
from django.urls import reverse_lazy
from django.db.models import Model, ForeignKey, ImageField, CASCADE
# from django.db.models.fields import CharField




# Create your models here.

class Categoria(Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField ('Nombre de la Categoría', max_length = 100, null = False, blank = False)
    estado = models.BooleanField ('Categoría Activada/Categoría Desactivada', default = True)
    fecha_creacion = models.DateField ('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Autor(Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length = 255, null = False, blank = False)
    apellido = models.CharField('Apellido', max_length = 255, null = False, blank = False)
    twitter = models.URLField('Twitter', null = True, blank = True)
    web = models.URLField('Web Site', null = True, blank = True)
    email = models.EmailField ('E-mail', null = False, blank = False)
    estado = models.BooleanField('Autor Activo/Autor Inactivo', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return f'Autor: {self.nombre} {self.apellido}'

class Post(Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título', max_length = 100, blank = False, null = False)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField('Descripción', max_length=255, blank=False, null=False)
    contenido = RichTextField()
    imagen = models.URLField('Imagen', max_length=255, blank=False, null=False)
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False)
    estado = models.BooleanField('Publicado/No Publicado', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo
    
class Avatar(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    imagen = ImageField(upload_to= 'avatares', null=True, blank= True)