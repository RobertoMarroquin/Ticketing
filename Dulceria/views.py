from django.shortcuts import render,redirect

from django.views.generic import DetailView
from django.views import View

from Facturacion.views import LineaVentaSession,CarritoSession
from .models import Combo,Golosina

# Create your views here.

class DulceriaView(View):
    def get(self, request):
        combos,golosinas = [],[]
        try:
            combos = Combo.objects.filter(disponibilidad=True)
            golosinas = Golosina.objects.filter(disponibilidad=True)

        except ObjectDoesNotExist:
            raise Http404("No se han encontrado Peliculas")
        

        context = {}
        context["combos"]=combos
        context["golosinas"]=golosinas

        return render(request,'Dulceria/dulceria.html',context)

    def post(self, request,):
        return HttpResponse('POST request!')    


class GolosinaView(View):
    def get(self, request, id):
        golosina = Golosina.objects.get(id=id)
        print(request.session.items())

        return render(request,"Dulceria/golosina.html",{'golosina':golosina})

    def post(self, request,id):

        print(CarritoSession(request))

        golosina = Golosina.objects.get(id=id)
        cantidad = int(request.POST["cantidad"])
        

        if cantidad != 0:
            LineaVentaSession(request,'g',golosina.id,cantidad)

        return redirect("dulceria:catalogo")


class ComboView(View):
    def get(self, request, id):
        combo = Combo.objects.get(id=id)
        print(request.session.items())

        return render(request,"Dulceria/combo.html",{'combo':combo})

    def post(self, request,id):

        print(CarritoSession(request))

        combo = Combo.objects.get(id=id)
        cantidad = int(request.POST["cantidad"])
        

        if cantidad != 0:
            LineaVentaSession(request,'g',combo.id,cantidad)

        return redirect("dulceria:catalogo")
