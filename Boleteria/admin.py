from django.contrib import admin

from .models import Butaca,Pelicula,Sala,Funcion,Boleteria

class ModelButacas(admin.StackedInline):
    model=Butaca
    extra=0

class ModelSalas(admin.ModelAdmin):
    inlines=[modelButacas]

class ModelPelicula(admin.StackedInline):
    model=Pelicula
    extra=0

class ModelFuncion(admin.ModelAdmin):
    inlines=[ModelPelicula]

# Register your models here.
admin.site.register(Boleteria)
admin.site.register(Pelicula,ModelFuncion)
admin.site.register(Funcion)
admin.site.register(Sala,ModelSalas)
