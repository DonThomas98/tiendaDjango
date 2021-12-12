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
from .views import *

urlpatterns = [

    path('', base, name='hogar'),

    path('faq', faq, name='faq'),  # PREGUNTAS FRECUENTES

    path('catalogo/busqueda/', busquedaView.as_view(), name='busqueda'),  # BUSQUEDA DE PRODUCTOS EN LA BARRA

    path('catalogo/perfumes', Catalogo_Perfume_ListView.as_view(), name='catalogoPerfumes'),
    path('catalogo/perfumes/<int:id_producto>/', ver_perfume, name='ver_perfume'),

    path('catalogo/decoracion', catalogo_decoracion, name='catalogoDecoracion'),
    path('catalogo/decoracion/<int:id_producto>/', ver_decoracion, name='ver_decoracion'),

    path('catalogo/dormitorio', catalogo_dormitorio, name='catalogoDormitorio'),
    path('catalogo/dormitorio/<int:id_producto>/', ver_dormitorio, name='ver_dormitorio'),

    path('contacto', ContactoCreateView.as_view(), name='contacto'),

]
