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
    path('login/',login_page,name="login_page"),
    path('logout/',logout_view,name="logout_view"),
    path('',admin_menu,name="admin_menu"),

    path('adminSalas/',adminSalas,name="adminSalas"),
    path('adminSalas/<int:sala_id>/',adminDetalleSala,name="adminDetalleSala"),
    path('adminSalas/crearSala/',adminCrearSala,name="adminCrearSala"),
    path('adminSalas/editarSala/<int:sala_id>/',adminEditarSala,name="adminEditarSala"),
    path('adminSalas/ded/',adminEliminarSala,name="adminEliminarSala"),
    path('adminSalas/born/',adminGuardarNuevaSala,name="adminGuardarNuevaSala"),
    path('adminSalas/upd/',adminActualizarSala,name="adminActualizarSala"),
    path('adminSalas/btcs/',darButacas,name="darButacas"),
    path('adminSalas/peekar/<int:id>/',peekar,name="peekar"),

    path('adminBoleterias/',adminBoleterias,name="adminBoleterias"),
    path('adminBoleterias/ded/',adminEliminarBoleteria,name="adminEliminarBoleteria"),
    path('adminBoleterias/<int:id>/',adminEditarBoleteria,name="adminEditarBoleteria"),
    path('adminBoleterias/crearBoleteria/',adminCrearBoleteria,name="adminCrearBoleteria"),

    path('adminFunciones/',adminFunciones,name="adminFunciones"),

    path('adminPeliculas/',adminPeliculas,name="adminPeliculas"),
]
