from django.contrib import admin
from .models import Producto, Sucursal, Venta, DetalleVenta, Categoria

# Register your models here.
admin.site.register(Producto)
admin.site.register(Sucursal)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Categoria)
