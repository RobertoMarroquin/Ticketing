from django.forms import ModelForm
from Boleteria.models import *

class boleteriaForm (ModelForm):
    class Meta:
        model=Boleteria
        fields="__all__"
