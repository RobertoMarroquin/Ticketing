from django.contrib import admin
from .models import Dulceria, Combo,Golosina,DetalleCombo
# Register your models here.

class DulceriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','eslogan','logo',)

class GolosinaAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio','descripcion','disponibilidad')

class ComboAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio','disponibilidad' )

class DetalleComboAdmin(admin.ModelAdmin):
    #list_display = ('get_combo','get_golosina','cantidad')
    list_display = ('combo','golosina','cantidad')
    list_filter = (
        ('combo',admin.RelatedOnlyFieldListFilter),
        ('golosina',admin.RelatedOnlyFieldListFilter),
    )
    # def get_golosina(self, obj):
    #     return obj.golosina.nombre

    # def get_combo(self, obj):
    #     return obj.combo.nombre
    # get_golosina.admin_order_field = 'nombre'
    # get_combo.admin_order_field  = 'nombre'
    # get_golosina.short_description = 'Nombre Golosina'
    # get_combo.short_description = 'Nombre Combo'


admin.site.register(DetalleCombo, DetalleComboAdmin)
admin.site.register(Combo, ComboAdmin)
admin.site.register(Golosina, GolosinaAdmin)
admin.site.register(Dulceria, DulceriaAdmin)
