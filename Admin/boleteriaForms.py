from django.forms import *
from Boleteria.models import *

class boleteriaForm (ModelForm):
    class Meta:
        model=Boleteria
        fields="__all__"

class funcionForm (ModelForm):
    class Meta:
        model=Funcion
        fields="__all__"
        widgets={
            'fecha': DateInput(format=('%d-%m-%Y'), attrs={
                                                           'type':"date",
                                                           'id': 'fechaForm',
                                                           'value':'%Y-%m-%d',
                                                           }),
            'hora': TimeInput(format=('%H:%M'),attrs={
                                                    'hidden':'true',
                                                    'id':'horaForm',
                                                    'value': '%H:%M',
            }),
       }

class peliculaForm (ModelForm):
    class Meta:
        model=Pelicula
        fields="__all__"
