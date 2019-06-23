from django.shortcuts import render

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