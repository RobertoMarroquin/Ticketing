from django.urls import path
from .views import FuncionList,FuncionView,PeliculaView,seleccionButacas,darButacas
urlpatterns = [
    path('cartelera/', FuncionList.as_view(), name='cartelera'),
    path('cartelera/<int:peli>', PeliculaView.as_view(), name='funciones'),
    path('funcion/<int:id>', FuncionView.as_view(), name='funcion'),
    path("funcion/butacas/",seleccionButacas,name="seleccionButacas"),
    path('gimme/',darButacas,name="darButacas"),
]
