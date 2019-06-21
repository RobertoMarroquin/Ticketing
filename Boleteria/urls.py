from django.urls import path
from .views import FuncionList,FuncionView,PeliculaView
urlpatterns = [
    path('cartelera/', FuncionList.as_view(), name='cartelera'),
    path('cartelera/<int:peli>', PeliculaView.as_view(), name='funciones'),
    path('funcion/<int:id>', FuncionView.as_view(), name='funcion'),
]