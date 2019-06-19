from django.shortcuts import render
from .models import Carrito,Cliente,TarjetaCredito,LineaVenta
from Boleteria.models import Boleto
from Dulceria.models import Combo, Golosina


import uuid

# Create your views here.

def CarritoSession(request):
    if not "tiene_carrito" in request.session:
        request.session['tiene_carrito'] = False

    if request.session["tiene_carrito"]:
        return request.session['carrito']
        
    else:    
        carrito = Carrito.objects.create()
        carrito.save()
        request.session["carrito"] = carrito.id
        request.session["tiene_carrito"] = True
        return request.session['carrito']
    

def LineaVentaSession(request,tipoProducto,idProducto,cantidad):
    
    carrito = Carrito.objects.get(id=request.session['carrito'])
    if tipoProducto =='b':
        boleto = Boleto.objects.get(id=idProducto)
        LineaVenta.objects.create(nombreProducto=boleto.tipo_cliente,
                                    tipoProducto=tipoProducto,
                                    idProducto=boleto.id,
                                    cantidad=cantidad,
                                    precio=boleto.precio,
                                    subtotal=cantidad * boleto.precio,
                                    carrito=carrito)

    elif tipoProducto == 'c' :
        combo = Combo.objects.get(id=idProducto)
        LineaVenta.objects.create(nombreProducto=combo.nombre,
                                    tipoProducto=tipoProducto,
                                    idProducto=combo.id,
                                    cantidad=cantidad,
                                    precio=combo.precio,
                                    subtotal=cantidad * combo.precio,
                                    carrito=carrito)
    
    elif tipoProducto == 'g' :
        golosina = Golosina.objects.create(nombreProducto=golosina.nombre,
                                    tipoProducto=tipoProducto,
                                    idProducto=golosina.id,
                                    cantidad=cantidad,
                                    precio=golosina.precio,
                                    subtotal=cantidad * golosina.precio,
                                    carrito=carrito)

