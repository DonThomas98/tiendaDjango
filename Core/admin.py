from django.contrib import admin
from .models import Producto, Sucursal, Venta, DetalleVenta, Categoria,Contacto,Marca

# Register your models here.
admin.site.register(Producto)
admin.site.register(Sucursal)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Categoria)
admin.site.register(Contacto)
admin.site.register(Marca)
