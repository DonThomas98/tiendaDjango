from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Producto,Categoria
from pytz import timezone

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

##Listado de productos como 
class ProductoList(ListView):
    model = Producto
    paginate_by =10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context