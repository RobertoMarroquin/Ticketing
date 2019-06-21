from django.db import models
from Boleteria.models import *
from Dulceria.models import *

import uuid

class Carrito(models.Model):
    """Model definition for Carrito."""

    creado = models.DateTimeField(("Fecha de Creacion"),auto_now_add = True)
    total = models.DecimalField(("Total"), max_digits=6, decimal_places=2,default=0)
    cantidadProductos = models.IntegerField(("Cantidad de Productos"),default=0)
    tipoPago = models.CharField(("Tipo de Pago"), max_length=50,blank=True, null=True)
    entregado = models.BooleanField(("Entregado"),default=False)
    cancelado = models.BooleanField(("Cancelado"),default=False)
    codigoCompra = models.CharField(("Codigo de Compra"),max_length=40,default=uuid.uuid4(),editable=False)
    tarjeta = models.ForeignKey('TarjetaCredito', on_delete=models.CASCADE,blank=True, null=True)

    class Meta:
        """Meta definition for Carrito."""

        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'

    def __str__(self):
        """Unicode representation of Carrito."""
        return f"{self.id} f{self.creado}"


class LineaVenta(models.Model):
    """Model definition for LineaVenta."""
    nombreProducto = models.CharField(("Nombre"), max_length=50)
    cantidad = models.IntegerField("Cantidad")
    tipoProducto = models.CharField(("Tipo de Producto"),max_length=100, blank=True, null=True)
    idProducto = models.IntegerField(("idProducto")) #Llave Foranea 
    precio = models.DecimalField(("Precio"), max_digits=6, decimal_places=2)
    subtotal = models.DecimalField(("subtotal"), max_digits=5, decimal_places=2)
    
    carrito = models.ForeignKey('Carrito', related_name='carrito', on_delete=models.CASCADE)
    class Meta:
        """Meta definition for LineaVenta."""

        verbose_name = 'LineaVenta'
        verbose_name_plural = 'LineaVentas'

    def __str__(self):
        """Unicode representation of LineaVenta."""
        return f'{self.nombreProducto} {self.cantidad}'


class Cliente(models.Model):
    """Model definition for Cliente."""
    nombre = models.CharField(("Nombre"),max_length=100, blank=True, null=True)
    correo = models.EmailField(("Correo Electronico"), max_length=254)

    class Meta:
        """Meta definition for Cliente."""

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        """Unicode representation of Cliente."""
        return f'{self.nombre }'


class TarjetaCredito(models.Model):
    """Model definition for TajetaCredito."""

    numero = models.IntegerField(("Numero"))
    fechaVencimiento = models.DateField(("Fecha Vencimiento"), auto_now=False, auto_now_add=False)
    ccv = models.IntegerField(("CCV"))
    marca = models.CharField(("Marca"), max_length=50)
    titular = models.ForeignKey('Cliente', related_name='titular', on_delete=models.CASCADE)


    class Meta:
        """Meta definition for TajetaCredito."""

        verbose_name = 'Tajeta de Credito'
        verbose_name_plural = 'TajetaCreditos'

    def __str__(self):
        """Unicode representation of TajetaCredito."""
        return f'{self.numero}'

