from django import forms
from .models import Contacto, Producto


class contacto_form(forms.Form):
    nombre = forms.CharField(label='Your name', max_length=100)
    correo = forms.EmailField()
    tipo_contacto = forms.IntegerField()
    mensaje = forms.CharField(label='Your name', max_length=100)
    avisos = forms.BooleanField()


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
