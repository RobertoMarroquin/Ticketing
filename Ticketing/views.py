from Boleteria.models import Sala
from Ticketing.salaForm import salaForm
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404

def adminSalas(request):
    salas=Sala.objects.all()
    return render(request,"administrador/adminSalas.html",{'salas':salas})

def adminDetalleSala(request,sala_id):
    sala = get_object_or_404(Sala, pk=sala_id)
    return render(request,'administrador/adminDetalleSala.html',{'sala':sala})

def adminCrearSala(request):
        if request.method == 'POST':
            form=salaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('adminSalas')
        else:
            form=salaForm()

        return render(request,'administrador/adminCrearSala.html',{'form':form})

def adminEditarSala (request,sala_id):
    sala = get_object_or_404(Sala,pk=sala_id)
    if request.method=="POST":
        form=salaForm(request.POST,instance=sala)
        if form.is_valid():
            form.save()
            return redirect ('adminDetalleSala',sala_id)
    else:
        form=salaForm(instance=sala)
    return render(request,'administrador/adminCrearSala.html',{'form':form})
