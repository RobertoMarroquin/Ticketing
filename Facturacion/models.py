from django.db import models
from Boleteria.models import *
from Dulceria.models import *


class Carrito(models.Model):
    """Model definition for Carrito."""

    total = models.DecimalField(("Total"), max_digits=6, decimal_places=2)
    cantidadProductos = models.IntegerField(("Cantidad de Productos"))
    tipoPago = models.CharField(("Tipo de Pago"), max_length=50)
    tiempoRestante = models.TimeField(("Tiempo Restante"), auto_now=False, auto_now_add=False)
    entregado = models.BooleanField((""))
    cancelado = models.BooleanField((""))
    codigoCompra = models.CharField(("Codigo Compra"), max_length=50)
    tarjeta = models.ForeignKey('TarjetaCredito', on_delete=models.CASCADE)


    class Meta:
        """Meta definition for Carrito."""

        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'

    def __str__(self):
        """Unicode representation of Carrito."""
        return self.total


class LineaVenta(models.Model):
    """Model definition for LineaVenta."""
    nombreProducto = models.CharField(("Nombre"), max_length=50)
    cantidad = models.IntegerField(())
    tipoProducto = models.CharField(max_length=100, blank=True, null=True)
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
    nombre = models.CharField(max_length=100, blank=True, null=True)
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

    numero = models.IntegerField((""))
    fechaVencimiento = models.DateField((""), auto_now=False, auto_now_add=False)
    ccv = models.IntegerField((""))
    marca = models.CharField((""), max_length=50)
    titular = models.ForeignKey('Cliente', related_name='titular', on_delete=models.CASCADE)


    class Meta:
        """Meta definition for TajetaCredito."""

        verbose_name = 'Tajeta de Credito'
        verbose_name_plural = 'TajetaCreditos'

    def __str__(self):
        """Unicode representation of TajetaCredito."""
        return f'{self.numero}'

