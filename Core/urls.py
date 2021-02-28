"""tiendaWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import base, faq, listar_perfumes, ficha_producto, ContactoForm,contacto2,listar_decoracion,\
    listar_dormitorio,agregar_producto

urlpatterns = [

    path('', base, name='hogar'),
    path('faq', faq, name='faq'),
    path('catalogo/perfumes', listar_perfumes, name='catalogoPefumes'),
    path('catalogo/decoracion', listar_decoracion, name='catalogoDecoracion'),
    path('catalogo/dormitorio', listar_dormitorio, name='catalogoDormitorio'),
    path('catalogo/ficha/int:id', ficha_producto, name='fichaProducto'),
    path('contacto', contacto2, name='contacto'),
    path('administrador/nuevo_producto', agregar_producto, name='administradorNuevoProducto'),
]
