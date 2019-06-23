from Boleteria.models import *
from Admin.salaForm import salaForm
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
import json
from django.core import serializers
from django.template import RequestContext
from Admin.loginForm import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_page')
def logout_view(request):
    logout(request)
    return redirect ("login_page")

def login_page(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    message = "Te has identificado de modo correcto"
                    return redirect("admin_menu")
                else:
                    message = "Tu usaurio esá inactivo"
            else:
                message = "Nombre de usuario y/o contraseña incorrecto"
    else:
        form = LoginForm()

    return render(request,"administrador/adminLogin.html",{"message":message,"form":form})

@login_required(login_url='login_page')
def admin_menu(request):
    return render (request,"administrador/adminMenu.html")

@login_required(login_url='login_page')
def peekar(request,id):
    s=Sala.objects.get(pk=id);
    f=s.numero_filas
    c=s.numero_columnas
    return render (request,'administrador/peekar.html',{'id':id,'f':f,'c':c})

@login_required(login_url='login_page')
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

@login_required(login_url='login_page')
def darButacas(request):
    laSala = Sala.objects.get(pk=request.POST['mensaje1'])
    lesButacas = Butaca.objects.filter(Sala=request.POST['mensaje1'])
    p=serializers.serialize('json', lesButacas)
    return HttpResponse(p)

@login_required(login_url='login_page')
def adminActualizarSala(request):
    sala_JSON=json.loads(request.POST['mensaje1'])
    butacas_JSON=json.loads(request.POST['mensaje2'])
    s=Sala.objects.get(pk=request.POST['mensaje3'])
    Butaca.objects.filter(Sala=s).delete()

    s.nombre=sala_JSON["nombre"]
    s.numero_sala=sala_JSON["numero_sala"]
    s.numero_asientos=sala_JSON["numero_asientos"]
    s.numero_filas=sala_JSON["numero_filas"]
    s.numero_columnas=sala_JSON["numero_columnas"]
    s.clase=sala_JSON["clase"]
    s.boleteria=Boleteria.objects.get(pk=sala_JSON["boleteria"])
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

@login_required(login_url='login_page')
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

@login_required(login_url='login_page')
def adminSalas(request):
    boleterias=Boleteria.objects.all()
    return render(request,"administrador/adminSalas.html",{'boleterias':boleterias})

@login_required(login_url='login_page')
def adminDetalleSala(request,sala_id):
    sala = get_object_or_404(Sala, pk=sala_id)
    return render(request,'administrador/adminDetalleSala.html',{'sala':sala})

@login_required(login_url='login_page')
def adminCrearSala(request):
    form=salaForm()
    return render(request,'administrador/adminCrearSala.html',{'form':form})

@login_required(login_url='login_page')
def adminEditarSala (request,sala_id):
    sala = get_object_or_404(Sala,pk=sala_id)
    form=salaForm(instance=sala)
    return render(request,'administrador/adminEditarSala.html',{'form':form,'id':sala_id})
