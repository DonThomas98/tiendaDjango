from django.shortcuts import render


# Create your views here.

def base(request):
    return render(request, 'base.html')
