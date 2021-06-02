from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from .models import Producto, Categoria, Contacto
from pytz import timezone
from .forms import ContactoForm
from django.urls import reverse_lazy
from django.db.models import Q


# Create your views here.

def base(request):
    data = {
    }

    return render(request, 'home.html', data)


def faq(request):
    return render(request, 'faq.html')

#def catalogo_perfumes(request):
 #   perfumes = Producto.objects.all().filter(categoria=2)

  #  data = {
   #     'prod': perfumes,
    #    'tipo_producto': 'Perfumes'

    #}
    #return render(request, 'catalogo/perfumes.html', data)


class Catalogo_Perfume_ListView(ListView):
    template_name = 'catalogo/perfumes.html'
    queryset = perfumes = Producto.objects.all().filter(categoria=2)
    paginate_by = 12



def ver_perfume(request, id_producto):
    producto = Producto.objects.filter(pk=id_producto)
    contexto = {
        'productos': producto,
        'formalidad': 'Perfume',

    }
    print(contexto)
    return render(request, 'catalogo/Fichas_productos/ficha_perfume.html', contexto)


def catalogo_decoracion(request):
    decoracion = Producto.objects.all().filter(categoria=1)

    data = {
        'prod': decoracion,
        'tipo_producto': 'Decoracion'

    }
    return render(request, 'catalogo/decoracion.html', data)


def ver_decoracion(request, id_producto):
    producto = Producto.objects.filter(pk=id_producto)
    contexto = {
        'productos': producto,
        'formalidad': 'Decoracion',
    }
    print(contexto)
    return render(request, 'catalogo/Fichas_productos/ficha_decoracion.html', contexto)


def catalogo_dormitorio(request):
    dormitorio = Producto.objects.all().filter(categoria=3)

    data = {
        'prod': dormitorio,
        'tipo_producto': 'Dormitorio'

    }
    return render(request, 'catalogo/dormitorio.html', data)


def ver_dormitorio(request, id_producto):
    producto = Producto.objects.filter(pk=id_producto)
    contexto = {
        'productos': producto,
        'formalidad': 'Dormitorio'
    }
    return render(request, 'catalogo/Fichas_productos/ficha_dormitorio.html', contexto)


class ContactoCreateView(CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'contacto/formulario_contacto.html'
    success_url = reverse_lazy('hogar')


class busquedaView(ListView):
    model = Producto
    template_name = 'barra_busqueda/busqueda_productos.html'

    def get_queryset(self):
        query = self.request.GET.get('buscar')
        object_list = Producto.objects.filter(
            Q(nombre__icontains=query)

        )
        return object_list


class PerfumeDetailView(DetailView):
    model = Producto




















