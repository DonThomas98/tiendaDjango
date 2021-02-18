from django.shortcuts import render


# Create your views here.

def base(request):
    return render(request, 'home.html')


def faq(request):
    return render(request, 'faq.html')


def listar_productos(request):
    data = {

    }
    render(request, data)
