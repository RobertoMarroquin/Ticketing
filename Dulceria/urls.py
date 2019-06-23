from django.urls import path
from .views import DulceriaView


urlpatterns = [
    path('catalogo/', DulceriaView.as_view(), name='catalogo'),
]
