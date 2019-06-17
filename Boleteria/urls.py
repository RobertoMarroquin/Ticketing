from django.urls import path
from .views import FuncionList,carousel
urlpatterns = [
    path('cartelera/', FuncionList.as_view(), name='catelera'),
    path('carousel/',carousel, name='micarousel'),
]