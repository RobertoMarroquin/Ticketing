from django.contrib import admin


from .models import Butaca,Pelicula,Sala,Funcion,Boleteria

# Register your models here.


admin.site.register(Boleteria)
admin.site.register(Pelicula)
admin.site.register(Funcion)
admin.site.register(Sala)
admin.site.register(Butaca)
