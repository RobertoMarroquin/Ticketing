from django.db import models

import datetime
# Create your models here.

class Boleteria(models.Model):
    """(Boleteria description)"""
    nombre = models.CharField(blank=True, max_length=100)
    eslogan = models.CharField(blank=True, max_length=100)
    logo = models.ImageField(upload_to="", blank=True, null=True)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    """(Pelicula description)"""

    nombre = models.CharField(blank=True, max_length=100)
    pais = models.CharField(blank=True, max_length=100)
    anyo = models.IntegerField(blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True)
    sinopsis = models.TextField(blank=True)
    clasificacion = models.CharField(blank=True, max_length=2)
    genero = models.CharField(blank=True, max_length=100)
    imagen = models.ImageField(upload_to="Peliculas",blank=True, null=True)
    boleteria = models.ForeignKey(Boleteria,on_delete=models.CASCADE)
    exhibicion = models.CharField(("En Exhibicion"),choices = [("exh","En Exhibicion"),("prx","Proximamente"),("ina","Inactiva")], max_length=50)

    def __str__(self):
        return self.nombre


class Sala(models.Model):
    """(Sala description)"""
    nombre = models.CharField(blank=True, max_length=100)
    numero_sala = models.IntegerField(blank=True, null=True)
    numero_asientos = models.IntegerField(blank=True, null=True)
    numero_filas = models.IntegerField(blank=True, null=True)
    numero_columnas = models.IntegerField(blank=True, null=True)
    clase = models.CharField(blank=True, max_length=100)
    boleteria = models.ForeignKey(Boleteria,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.nombre} {self.numero_sala}"


class Funcion(models.Model):
    """(Funcion description)"""
    hora = models.TimeField(blank=True)
    fecha = models.DateField(default=datetime.datetime.today)
    lenguaje = models.CharField(blank=True, max_length=100)
    formato = models.CharField(choices=[('2D','2D'),('3D','3D'),('XD','XD')],blank=True, max_length=100)
    estado = models.BooleanField(default=True)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pelicula} {self.sala.numero_sala} {self.fecha} {self.hora}"


class Boleto(models.Model):
    """(Boleto description)"""
    tipo_cliente = models.CharField(blank=True, max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    descripcion = models.TextField(blank=True)
    Funcion = models.ManyToManyField(Funcion,blank=True)

    def __str__(self):
        return f"{self.tipo_cliente} ${self.precio}"


class Butaca(models.Model):
    """(Butaca description)"""
    numero_asiento = models.IntegerField(blank=True, null=True)
    fila = models.CharField(blank=True, max_length=2)
    disponibilidad = models.BooleanField(default=True)
    clase = models.BooleanField(default=True)
    Sala = models.ForeignKey(Sala,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fila}{self.numero_asiento}"
