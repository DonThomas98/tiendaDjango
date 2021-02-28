from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Producto, Categoria
from pytz import timezone
from .forms import contacto_form, ContactoForm, ProductoForm


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


def contacto(request):
    if request.method == 'POST':
        form = contacto_form(request.POST)
        if form.is_valid():
            return HttpResponse('Gracias por su tiempo!')
    else:
        form = contacto_form()

    data = {

        'form': form

    }
    return render(request, 'contacto/formulario_contacto.html', data)


def contacto2(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            return HttpResponse('Gracias por su tiempo!')
    else:
        form = ContactoForm()

    data = {

        'form': form

    }
    return render(request, 'contacto/formulario_contacto.html', data)


def agregar_producto(request):
    data = {

        'form': ProductoForm
    }

    return render(request, 'administrador/nuevo_producto.html', data)
