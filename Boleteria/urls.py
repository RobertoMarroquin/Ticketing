from django.urls import path
from .views import FuncionList
urlpatterns = [
    path('cartelera/', FuncionList.as_view(), name='catelera'),
]