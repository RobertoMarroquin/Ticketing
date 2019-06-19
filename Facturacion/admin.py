from django.contrib import admin
from .models import Carrito,Cliente,LineaVenta,TarjetaCredito
# Register your models here.

admin.site.register(Carrito)
admin.site.register(TarjetaCredito)
admin.site.register(LineaVenta)
admin.site.register(Cliente)
