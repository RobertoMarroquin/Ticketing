from django.shortcuts import render,redirect
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404,HttpResponse
from django.forms.models import model_to_dict
from django.core import serializers
from django.views.generic import ListView
from django.views.generic.edit import FormMixin


import datetime
import json

from .models import Butaca,Pelicula,Sala,Funcion,Boleteria,Boleto
from Facturacion.views import CarritoSession,LineaVentaSession
from Facturacion.models import LineaVenta,Carrito
# Create your views here.


def home(request):
    peliculas = Pelicula.objects.filter(exhibicion="exh")
    return render(request,'home.html',{'peliculas':peliculas})

class PeliculaView(View):
    def get(self, request, peli):
        try:
            pelicula = Pelicula.objects.get(id=peli)
            funciones = Funcion.objects.filter(pelicula=pelicula,fecha=datetime.date.today())
        except ObjectDoesNotExist:
            raise Http404("No se han encontrado Peliculas")
        
        context = { "pelicula":pelicula,
                    "funciones":funciones
        }
        return render(request,"Boleteria/cartelera.html",context)

    def post(self, request):
       
        return HttpResponse('POST request!')

class FuncionList(ListView):
    model = Funcion
    context_object_name = 'funciones'
    template_name='Boleteria/cartelera.html'
    ordering = ['fecha','hora']


class FuncionView(View):
    def get(self, request, id):
        funcion = Funcion.objects.get(id=id)
        print(request.session.items())

        return render(request,"Boleteria/funcion.html",{'funcion':funcion})

    def post(self, request,id):

        print(CarritoSession(request))

        funcion = Funcion.objects.get(id=id)
        adultos = int(request.POST["adultos"])
        ninos = int(request.POST["ninos"])
        mayores = int(request.POST["mayores"])
        

        if adultos != 0:
            boleto = Boleto.objects.get(tipo_cliente="Adulto")
            LineaVentaSession(request,'b',boleto.id,adultos)
            

        if ninos != 0:
            boleto = Boleto.objects.get(tipo_cliente="Nino")
            LineaVentaSession(request,'b',boleto.id,ninos)

        if mayores != 0:
            boleto = Boleto.objects.get(tipo_cliente="Mayor")
            LineaVentaSession(request,'b',boleto.id,mayores)

        return redirect("boleteria:cartelera")


class SeleccionButacas(View):
    def get(self, request, funcion):
        return render(request,"",{})

    def post(self, request):
        return render(request,"",{})


###-----Serializacion de listas de objetos    
#def get(self, request,fecha=datetime.date.today()):
#    fecha = fecha
#    funciones = list(Funcion.objects.filter(fecha=fecha))
#    listaJson = json.loads(serializers.serialize('json',funciones))
#    #serialized = json.dumps(dict_funcion)
#    print(funciones)
#    print(listaJson)
#    return render(REQUEST,".html",context = {'listaJson' : listaJson})
