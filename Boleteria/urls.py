from django.urls import path
from .views import FuncionList,Prueba,FuncionView
urlpatterns = [
    path('cartelera/', FuncionList.as_view(), name='cartelera'),
    path('funcion/<int:id>', FuncionView.as_view(), name='funcion'),
]