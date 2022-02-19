from django.forms import DateField, Form, ImageField, IntegerField, DecimalField, CharField, EmailField, URLField, SlugField, BooleanField
from django.db.models import CASCADE
from .models import Autor, Categoria
class AvatarFormulario(Form):
    imagen = ImageField(required=True)

""" class PostCreate(Form):
    id = AutoField(primary_key=True)
    titulo = Form.CharField('Título', max_length=100, blank=False, null=False)
    autor = Form.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria =ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = CharField('Descripción', max_length=255, blank=False, null=False)
    contenido = RichTextField()
    imagen = URLField('Imagen', max_length=255, blank=False, null=False)
    slug = SlugField('Slug', max_length=100, blank=False, null=False)
    estado = BooleanField('Publicado/No Publicado', default=True)
    fecha_creacion = DateField('Fecha de Creación', auto_now=False, auto_now_add=True) """
