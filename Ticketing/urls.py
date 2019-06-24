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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Boleteria.views import home,borrarCarritoJS,getNumCarrito

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cine/', include(('Boleteria.urls',"Boleteria"),namespace="boleteria")),
<<<<<<< HEAD
    path("", home, name="home"),
    path("dulceria/", include(('Dulceria.urls','Dulceria'),namespace='dulceria')),
    path("facturacion/", include(('Facturacion.urls','Facturacion'),namespace='facturacion')),
    path('adminSalas/',include('Admin.urls'),name='administracion'),
=======
    path('admin_ticketing/',include('Admin.urls'),name='administracion'),
    path("", home, name="home"),
    path("borrarCarritoJS/",borrarCarritoJS,name="borrarCarritoJS"),
    path("getNumCarrito/",getNumCarrito,name="getNumCarrito"),
>>>>>>> da3a90d83db983267c3d4c3360307b8937c258aa
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
