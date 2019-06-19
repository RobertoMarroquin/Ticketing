from django.contrib import admin

from .models import Butaca,Pelicula,Sala,Funcion,Boleteria

class ModelButacas(admin.StackedInline):
    model=Butaca
    extra=0

class ModelSalas(admin.ModelAdmin):
    inlines=[ModelButacas]

# Register your models here.
admin.site.register(Boleteria)
admin.site.register(Pelicula)
admin.site.register(Funcion)
admin.site.register(Sala,ModelSalas)
