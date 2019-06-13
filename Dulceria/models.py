from django.db import models

# Create your models here.

class Dulceria(models.Model):
    """(Dulceria description)"""
    nombre = models.CharField(blank=True, max_length=100)
    #logo = models.ImageField(upload_to="imagenes/", height_field=4000, width_field=4000)
    eslogan = models.CharField(blank=True, max_length=100)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __str__(self):
        return f"{self.nombre}"


class Golosina(models.Model):
    """(Golosina description)"""
    nombre = models.CharField(blank=True, max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.TextField(blank=True)
    #caducidad = models.DateField(default=datetime.datetime.today)
    disponibilidad = models.BooleanField(default=True)
    dulceria = models.ForeignKey(Dulceria,on_delete="CASCADE")

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __str__(self):
        return f"{self.nombre}"


class Combo(models.Model):

    nombre = models.CharField(blank=True, max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.TextField(blank=True)
    disponibilidad = models.BooleanField(default=True)
    dulceria = models.ForeignKey(Dulceria,on_delete="CASCADE")

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __str__(self):
        return f"{self.nombre}"


class DetalleCombo(models.Model):
    """(DetalleCombo description)"""
    combo = models.ForeignKey(Combo,on_delete=models.CASCADE)
    golosina = models.ForeignKey(Golosina,on_delete=models.CASCADE)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __str__(self):
        return f"{self.combo.id}-{self.golosina.id}"
