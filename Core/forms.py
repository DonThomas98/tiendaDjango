from django.forms import *
from django import forms
from .models import Contacto, Producto


class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        # exclude = []
        labels= {
        'nombre': 'Su nombre',
        'correo': 'Su correo',
        'tipo_contacto': 'Motivo de contacto'

        }

        widgets = {

            'mensaje':  Textarea(
                attrs={

                    'class': 'form-control',
                    'placeholder': 'Ingrese su mensaje',
                    'autocomplete': 'off'

                }
            ),
            'nombre':  TextInput(
                attrs={

                    'class': 'form-control',
                    'placeholder': 'Ingrese su Nombre',
                    'autocomplete': 'off'

                }
            ),
            'correo':  EmailInput(
                attrs={

                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo',
                    'autocomplete': 'on'

                }
            ),
            'tipo_contacto':  Select(
                attrs={

                    'class': 'form-control',
                    'placeholder': 'Motivo para contactarse',

                }
            ),


        }

