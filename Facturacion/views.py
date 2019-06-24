from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.views import View


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
        golosina = Golosina.objects.get(id=idProducto)
        LineaVenta.objects.create(nombreProducto=golosina.nombre,
                                    tipoProducto=tipoProducto,
                                    idProducto=golosina.id,
                                    cantidad=cantidad,
                                    precio=golosina.precio,
                                    subtotal=cantidad * golosina.precio,
                                    carrito=carrito)

class CarritoDetalle(View):
    def get(self, request):
        carrito = Carrito.objects.get(id=int(request.session['carrito']))
        lineasVentas = LineaVenta.objects.filter(carrito=carrito)

        boletos = LineaVenta.objects.filter(carrito=carrito,tipoProducto='b')
        golosinas = LineaVenta.objects.filter(carrito=carrito,tipoProducto='g')
        combos = LineaVenta.objects.filter(carrito=carrito,tipoProducto='c')

        context = {}
        context['lineasVentas'] = lineasVentas
        context['boletos'] = boletos
        context['golosinas'] = golosinas
        context['combos'] = combos
        context['carrito'] = carrito

        return render(request,'Facturacion/factura.html',context)

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')


class VentaView(View):
    def get(self, request):
        return render(request,'Facturacion/venta.html',{})

    def post(self, request):

        context = {}
        codigo = request.POST['codigo']
        cliente = request.POST['cliente']

        compra = Carrito.objects.filter(codigoCompra__endswith=codigo, tarjeta__cliente__nombre=cliente)
        
        if compra:
            items = LineaVenta.objects.filter(carrito=compra)
            context['compra'] = compra
            context['items'] = items
        else:
            context['error'] = 'Codigo Invalido'
        return render(request,'Facturacion/venta.html',context)
        




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect ('facturacion:venta')
        else:
            return render(request,'login.html',{   'error':'Usuario o contrasena invalidos',
                                                            'User':request.user.is_authenticated})
    return render(request,'login.html',{'User':request.user.is_authenticated})


def logout_func(request):
    logout(request)
    return redirect('facturacion:login')

    