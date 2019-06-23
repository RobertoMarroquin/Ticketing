from django.urls import path
from .views import CarritoDetalle


urlpatterns = [
    path('micarrito/', CarritoDetalle.as_view(), name='micarrito'),
]
