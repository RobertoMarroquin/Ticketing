from django.contrib import admin

from .models import Butaca,Pelicula,Sala,Funcion,Boleteria

class ModelButacas(admin.StackedInline):
    model=Butaca
    extra=0

class ModelBoleteria(admin.ModelAdmin):
    list_display = ('nombre','eslogan','logo')

class ModelSalas(admin.ModelAdmin):
    list_display = ('nombre','numero_sala','numero_asientos','clase','boleteria')
    list_filter=['boleteria','clase']
    inlines=[ModelButacas]

class ModelPelicula(admin.ModelAdmin):
    list_display = ('nombre','duracion','clasificacion','genero','boleteria')
    list_filter=['clasificacion','genero']

class ModelFuncion(admin.ModelAdmin):
    list_display = ('pelicula','sala','hora','fecha','lenguaje','formato','estado')
    list_filter=['pelicula','sala','fecha','lenguaje','formato','estado']

# Register your models here.
admin.site.register(Boleteria,ModelBoleteria)
admin.site.register(Pelicula,ModelPelicula)
admin.site.register(Funcion,ModelFuncion)
admin.site.register(Sala,ModelSalas)
