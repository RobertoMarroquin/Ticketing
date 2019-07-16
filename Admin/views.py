from Boleteria.models import *
from Admin.salaForm import salaForm
from Admin.boleteriaForms import *
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
def darButacasAdm(request):
    laSala = Sala.objects.get(pk=request.POST['mensaje1'])
    lesButacas = Butaca.objects.filter(Sala=request.POST['mensaje1'])
    p=serializers.serialize('json', lesButacas)
    return HttpResponse(p)

#///////////////////Salas/////////////////////
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
#/////////////////////////////////////////////

#/////////////////Boleteria///////////////////
@login_required(login_url='login_page')
def adminBoleterias(request):
    boleterias=Boleteria.objects.all()
    return render(request,"administrador/adminBoleterias.html",{'boleterias':boleterias})

@login_required(login_url='login_page')
def adminEliminarBoleteria(request):
    try:
        boleteria = Boleteria.objects.get(pk=request.POST['mensaje'])
    except boleteria.DoesNotExist:
        return HttpResponse ("-1")
    try:
        boleteria.logo.delete(save=True)
        boleteria.delete()
    except:
        return HttpResponse("0")

    return HttpResponse("1")

@login_required(login_url='login_page')
def adminEditarBoleteria (request,id):
    boleteria = get_object_or_404(Boleteria,pk=id)
    if request.method=="POST":
        imagenActual=boleteria.logo
        form=boleteriaForm(request.POST,request.FILES,instance=boleteria)

        try:
            formImagen=request.FILES['logo'].name
        except:
            formImagen=""

        if imagenActual!="" and formImagen!="":
            imagenActual.delete(save=True)

        if form.is_valid():
            if boleteria.logo!=imagenActual and boleteria.logo=="":
                imagenActual.delete(save=True)
            form.save()
            return redirect ('adminBoleterias')
    else:
        form=boleteriaForm(instance=boleteria)
    return render(request,'administrador/adminEditarBoleteria.html',{'form':form,'id':id})

@login_required(login_url='login_page')
def adminCrearBoleteria(request):
    if request.method == 'POST':
        form=boleteriaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('adminBoleterias')
    else:
        form=boleteriaForm()
    return render(request,'administrador/adminCrearBoleteria.html',{'form':form})
#/////////////////////////////////////////////

#/////////////////Funciones///////////////////
@login_required(login_url='login_page')
def adminFunciones(request):
    funciones=Funcion.objects.all()
    return render(request,"administrador/adminFunciones.html",{'funciones':funciones})

@login_required(login_url='login_page')
def adminDetalleFuncion(request,id):
    funcion = get_object_or_404(Funcion, pk=id)
    return render(request,'administrador/adminDetalleFuncion.html',{'funcion':funcion})

@login_required(login_url='login_page')
def adminEliminarFuncion(request):
    try:
        funcion = Funcion.objects.get(pk=request.POST['mensaje'])
    except boleteria.DoesNotExist:
        return HttpResponse ("-1")
    try:
        funcion.delete()
    except:
        return HttpResponse("0")

    return HttpResponse("1")

@login_required(login_url='login_page')
def adminEditarFuncion (request,id):
    funcion = get_object_or_404(Funcion,pk=id)
    if request.method=="POST":
        form=funcionForm(request.POST,instance=funcion)

        if form.is_valid():
            form.save()
            return redirect ('adminFunciones')
    else:
        form=funcionForm(instance=funcion)
    return render(request,'administrador/adminEditarFuncion.html',{'form':form,'id':id})

@login_required(login_url='login_page')
def adminCrearFuncion(request):
    if request.method == 'POST':
        form=funcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('adminFunciones')
    else:
        form=funcionForm()
    return render(request,'administrador/adminCrearFuncion.html',{'form':form})
#/////////////////////////////////////////////

#/////////////////peliculas///////////////////
@login_required(login_url='login_page')
def adminPeliculas(request):
    peliculas=Pelicula.objects.all()
    return render(request,"administrador/adminPeliculas.html",{'peliculas':peliculas})

@login_required(login_url='login_page')
def adminDetallePelicula(request,id):
    pelicula = get_object_or_404(Pelicula, pk=id)
    return render(request,'administrador/adminDetallePelicula.html',{'pelicula':pelicula})

@login_required(login_url='login_page')
def adminEliminarPelicula(request):
    try:
        pelicula = Pelicula.objects.get(pk=request.POST['mensaje'])
    except pelicula.DoesNotExist:
        return HttpResponse ("-1")
    try:
        pelicula.imagen.delete(save=True)
        pelicula.delete()
    except:
        return HttpResponse("0")

    return HttpResponse("1")

@login_required(login_url='login_page')
def adminEditarPelicula (request,id):
    pelicula = get_object_or_404(Pelicula,pk=id)
    if request.method=="POST":
        imagenActual=pelicula.imagen
        form=peliculaForm(request.POST,request.FILES,instance=pelicula)

        try:
            formImagen=request.FILES['imagen'].name
        except:
            formImagen=""

        if imagenActual!="" and formImagen!="":
            imagenActual.delete(save=True)

        if form.is_valid():
            if pelicula.imagen!=imagenActual and pelicula.imagen=="":
                imagenActual.delete(save=True)
            form.save()
            return redirect ('adminPeliculas')
    else:
        form=peliculaForm(instance=pelicula)
    return render(request,'administrador/adminEditarPelicula.html',{'form':form,'id':id})

@login_required(login_url='login_page')
def adminCrearPelicula(request):
    if request.method == 'POST':
        form=peliculaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('adminPeliculas')
    else:
        form=peliculaForm()
    return render(request,'administrador/adminCrearPelicula.html',{'form':form})
#/////////////////////////////////////////////
