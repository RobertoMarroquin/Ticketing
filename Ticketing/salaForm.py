from django.forms import ModelForm
from Boleteria.models import Sala

class salaForm (ModelForm):
    class Meta:
        model=Sala
        fields="__all__"
