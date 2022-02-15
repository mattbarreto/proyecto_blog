from django.contrib import admin
from app_blog.models import Categoria, Autor, Post
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class CategoriaResource(resources.ModelResource):
    class Meta:
        model: Categoria

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion',)
    resource_class = CategoriaResource

class AutorResouce(resources.ModelResource):
    class Meta:
        model: Autor

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre', 'apellido']
    list_display = ('nombre', 'apellido', 'email', 'estado', 'fecha_creacion',)
    resource_class = AutorResouce

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post,)