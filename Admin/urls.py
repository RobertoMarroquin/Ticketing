"""Ticketing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from Admin.views import *

urlpatterns = [
    path('',adminSalas,name="adminSalas"),
    path('<int:sala_id>/',adminDetalleSala,name="adminDetalleSala"),
    path('crearSala/',adminCrearSala,name="adminCrearSala"),
    path('editarSala/<int:sala_id>/',adminEditarSala,name="adminEditarSala"),
    path('ded/',adminEliminarSala,name="adminEliminarSala"),
    path('born/',adminGuardarNuevaSala,name="adminGuardarNuevaSala"),
    path('upd/',adminActualizarSala,name="adminActualizarSala"),
    path('btcs/',darButacas,name="darButacas"),
    path('peekar/<int:id>/',peekar,name="peekar"),
]
