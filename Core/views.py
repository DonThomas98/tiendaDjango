from django.shortcuts import render, HttpResponse
from .models import Producto


# Create your views here.

def base(request):
    return render(request, 'home.html')


def faq(request):
    return render(request, 'faq.html')


def listar_perfumes(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos,
    }
    return render(request, 'catalogo/perfumes.html', data)

##Listado de productos
