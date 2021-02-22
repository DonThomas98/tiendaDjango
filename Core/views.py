from django.shortcuts import render, HttpResponse
from .models import Producto,Categoria

# Create your views here.

def base(request):
    return render(request, 'home.html')


def faq(request):
    return render(request, 'faq.html')


def listar_perfumes(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    data = {
        'prod': productos,
        'categorias':categorias,
    }
    return render(request, 'perfumes.html', data)

##Listado de productos
