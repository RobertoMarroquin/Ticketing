from django.urls import path
from .views import DulceriaView,GolosinaView,ComboView


urlpatterns = [
    path('catalogo/', DulceriaView.as_view(), name='catalogo'),
    path('golosina/<int:id>', GolosinaView.as_view(), name='dulce'),
    path('combo/<int:id>', ComboView.as_view(), name='combo'),
]
