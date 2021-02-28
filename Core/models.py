from django.db import models


# Create your models here.

class Sucursal(models.Model):
    nombre_sucursal = models.CharField(max_length=50)
    direccion_sucursal = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    opcionesCategoria = [
        ('DC', 'Decoración'),
        ('PF', 'Perfumes'),
        ('DR', 'Dormitorio'),
    ]

    categoria = models.CharField(max_length=15, choices=opcionesCategoria)

    def __str__(self):
        return self.categoria

    class Meta:
        db_table = 'categoria'


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    foto = models.ImageField(upload_to='media/', default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200, default='No hay descripción')

    def __str__(self):
        return '%s %s' % (self.nombre, self.categoria)

    class Meta:
        db_table = 'producto'
        ordering = ['id']


class Venta(models.Model):
    monto_venta = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"


class DetalleVenta(models.Model):
    fecha_venta = models.DateField(auto_now=True)
    sucursal = models.ManyToManyField(Sucursal)

    def __str__(self):
        return self.name


class Contacto(models.Model):
    opcionesContacto = [
        ('0', 'Contacto'),
        ('1', 'Reclamo'),
        ('2', 'Problema al momento de comprar'),
        ('3', 'Sugerencias'),
        ('4', 'Felicitaciones'),
    ]

    nombre = models.CharField(max_length=70)
    correo = models.EmailField()
    tipo_contacto = models.IntegerField(choices=opcionesContacto)
    mensaje = models.CharField(max_length=200)
    avisos = models.BooleanField(blank=True)


def __str__(self):
    return '%s %s' % (self.nombre, self.tipo_contacto)

