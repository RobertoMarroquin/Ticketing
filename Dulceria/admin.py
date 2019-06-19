from django.contrib import admin
from .models import Dulceria, Combo,Golosina,DetalleCombo
# Register your models here.

class DulceriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','eslogan','logo',)

class GolosinaAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio','descripcion','disponibilidad')

class DetalleComboAdmin(admin.StackedInline):
    model=DetalleCombo
    extra=0

class ComboAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio','disponibilidad')
    inlines=[DetalleComboAdmin]

admin.site.register(Combo, ComboAdmin)
admin.site.register(Golosina, GolosinaAdmin)
admin.site.register(Dulceria, DulceriaAdmin)
