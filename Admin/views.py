from Boleteria.models import *
from Admin.salaForm import salaForm
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
import json
from django.core import serializers

def peekar(request,id):
    s=Sala.objects.get(pk=id);
    f=s.numero_filas
    c=s.numero_columnas
    return render (request,'administrador/peekar.html',{'id':id,'f':f,'c':c})

def adminEliminarSala(request):
    sala_id=request.POST['mensaje']
    try:
        sala = Sala.objects.get(pk=sala_id)
    except sala.DoesNotExist:
        return HttpResponse ("-1")
    try:
        sala.delete()
    except:
        return HttpResponse("0")

    return HttpResponse("1")

def darButacas(request):
    laSala = Sala.objects.get(pk=request.POST['mensaje1'])
    lesButacas = Butaca.objects.filter(Sala=request.POST['mensaje1'])
    p=serializers.serialize('json', lesButacas)
    return HttpResponse(p)

def adminActualizarSala(request):
    sala_JSON=json.loads(request.POST['mensaje1'])
    butacas_JSON=json.loads(request.POST['mensaje2'])
    Sala.objects.get(pk=request.POST['mensaje3']).delete()

    s=Sala(
           nombre=sala_JSON["nombre"],
           numero_sala=sala_JSON["numero_sala"],
           numero_asientos=sala_JSON["numero_asientos"],
           numero_filas=sala_JSON["numero_filas"],
           numero_columnas=sala_JSON["numero_columnas"],
           clase=sala_JSON["clase"],
           boleteria=Boleteria.objects.get(pk=sala_JSON["boleteria"])
           )
    s.save()

    for w in butacas_JSON:
        b=Butaca(
               numero_asiento=w["numero_asiento"],
               fila=w["fila"],
               disponibilidad=w["disponibilidad"],
               clase=w["clase"],
               Sala=Sala.objects.get(pk=s.id)
               )
        b.save()
    return HttpResponse ("DONE")

def adminGuardarNuevaSala(request):
    sala_JSON=json.loads(request.POST['mensaje1'])
    butacas_JSON=json.loads(request.POST['mensaje2'])

    s=Sala(
           nombre=sala_JSON["nombre"],
           numero_sala=sala_JSON["numero_sala"],
           numero_asientos=sala_JSON["numero_asientos"],
           numero_filas=sala_JSON["numero_filas"],
           numero_columnas=sala_JSON["numero_columnas"],
           clase=sala_JSON["clase"],
           boleteria=Boleteria.objects.get(pk=sala_JSON["boleteria"])
           )
    s.save()

    for w in butacas_JSON:
        b=Butaca(
               numero_asiento=w["numero_asiento"],
               fila=w["fila"],
               disponibilidad=w["disponibilidad"],
               clase=w["clase"],
               Sala=Sala.objects.get(pk=s.id)
               )
        b.save()
    return HttpResponse ("DONE")

def adminSalas(request):
    boleterias=Boleteria.objects.all()
    return render(request,"administrador/adminSalas.html",{'boleterias':boleterias})

def adminDetalleSala(request,sala_id):
    sala = get_object_or_404(Sala, pk=sala_id)
    return render(request,'administrador/adminDetalleSala.html',{'sala':sala})

def adminCrearSala(request):
    form=salaForm()
    return render(request,'administrador/adminCrearSala.html',{'form':form})

def adminEditarSala (request,sala_id):
    sala = get_object_or_404(Sala,pk=sala_id)
    form=salaForm(instance=sala)
    return render(request,'administrador/adminEditarSala.html',{'form':form,'id':sala_id})
