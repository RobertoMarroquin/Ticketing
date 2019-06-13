from django.shortcuts import render
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404,HttpResponse
from django.forms.models import model_to_dict
from django.core import serializers
from django.views.generic import ListView


import datetime
import json

from .models import Butaca,Pelicula,Sala,Funcion,Boleteria
# Create your views here.

class PeliculaView(View):
    def get(self, request, peli):
        try:
            pelicula = Pelicula.objects.get(id=peli)
            funciones = Funcion.objects.filter(pelicula=pelicula,fecha=datetime.date.today())
        except ObjectDoesNotExist:
            raise Http404("No se han encontrado Peliculas")
        cotext = {"pelicula":pelicula,
            "funciones":funciones
        }
        return render(request,"detallePelicula",context)

    def post(self, request):
        adultos = int(request.POST['adultos'])
        ninos = int(request.POST['ninos'])
        terceraEdad = int(request.POST["terceraEdad"])
        estudiantes = int(request.POST["estudiantes"])
        funcion = request.POST["funcion"]
        for i in range(adultos):
            boleto = Boleto.create(funcion=funcion)
        return HttpResponse('POST request!')

class FuncionList(ListView):
    model = Funcion
    context_object_name = 'funciones'
    template_name='Boleteria/cartelera.html'


def carousel(request):

    return render(request,"Boleteria/carousel.html",{})
    
###-----Serializacion de listas de objetos    
#def get(self, request,fecha=datetime.date.today()):
#    fecha = fecha
#    funciones = list(Funcion.objects.filter(fecha=fecha))
#    listaJson = json.loads(serializers.serialize('json',funciones))
#    #serialized = json.dumps(dict_funcion)
#    print(funciones)
#    print(listaJson)
#    return HttpResponse(fecha)

    