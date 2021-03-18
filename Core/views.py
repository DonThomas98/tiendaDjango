from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, CreateView
from .models import Producto, Categoria, Contacto
from pytz import timezone
from .forms import ContactoForm
from django.urls import reverse_lazy


# Create your views here.

def base(request):
    return render(request, 'home.html')


def faq(request):
    return render(request, 'faq.html')


def listar_perfumes(request):
    productos = Producto.objects.all().filter(categoria_id=2)
    data = {
        'prod': productos,  # prod es lo que debe ir reflejado en el template
    }
    return render(request, 'catalogo/perfumes.html', data)


def listar_decoracion(request):
    productos = Producto.objects.all().filter(categoria_id=1)
    data = {
        'prod': productos,  # prod es lo que debe ir reflejado en el template
    }
    return render(request, 'catalogo/decoracion.html', data)


def listar_dormitorio(request):
    productos = Producto.objects.all().filter(categoria_id=3)
    data = {
        'prod': productos,  # prod es lo que debe ir reflejado en el template
    }
    return render(request, 'catalogo/dormitorio.html', data)


def ficha_producto(request):
    data = {

    }
    if request.method == 'GET':
        return 0
    return render(request, 'catalogo/ficha_producto.html')


class ContactoCreateView(CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'contacto/formulario_contacto.html'
    success_url = reverse_lazy('hogar')
