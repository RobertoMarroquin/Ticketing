from django.contrib import admin
from .models import Dulceria,Golosina,Combo,DetalleCombo
# Register your models here.

admin.site.site_header = 'Administra tus dulcerías'

class DulceriaAdmin(admin.ModelAdmin):
    '''Admin View for Dulceria'''
    list_display = ('nombre','eslogan',)
    list_filter = ('nombre',)
    list_editable = ('eslogan',)
    readonly_fields = ('nombre',)
    ordering = ('nombre',)
    

admin.site.register(Dulceria,DulceriaAdmin)
admin.site.register(Golosina)
admin.site.register(Combo)
admin.site.register(DetalleCombo)
