from django.db import models
from django.contrib.auth.models import User # Para relacionarlo con los usuarios

# El Vendedor se relaciona con un Usuario de Django para poder loguearse
class Vendedor(models.Model):
    # OneToOneField es un vínculo único. Un Vendedor tiene un solo Usuario, y viceversa.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    activo = models.BooleanField(default=True)

    # El método __str__ es para que los objetos se muestren de forma legible.
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    # DecimalField es ideal para dinero. Evita errores de redondeo.
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Entrega(models.Model):
    # ForeignKey es un vínculo de "muchos a uno". Un vendedor puede tener muchas entregas.
    # on_delete=models.CASCADE significa que si se borra un vendedor, se borran sus entregas.
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, related_name='entregas')
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    # `related_name` nos ayuda a acceder desde el modelo relacionado.

    def __str__(self):
        return f"Entrega a {self.vendedor} el {self.fecha_entrega.strftime('%d/%m/%Y')}"

class DetalleEntrega(models.Model):
    entrega = models.ForeignKey(Entrega, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario_congelado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

class Pago(models.Model):
    METODOS_PAGO = [
        ('Efectivo', 'Efectivo'),
        ('Transferencia', 'Transferencia'),
        ('Otro', 'Otro'),
    ]
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, related_name='pagos')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    metodo = models.CharField(max_length=50, choices=METODOS_PAGO, default='Efectivo')

    def __str__(self):
        return f"Pago de ${self.monto} de {self.vendedor}"

class Compra(models.Model):
    fecha_compra = models.DateField()
    proveedor = models.CharField(max_length=100, blank=True, null=True)
    total_calculado = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Compra del {self.fecha_compra.strftime('%d/%m/%Y')} a {self.proveedor}"

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='detalles')
    descripcion_producto = models.CharField(max_length=255)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Siempre guarda la descripción en mayúsculas
        self.descripcion_producto = self.descripcion_producto.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cantidad} x {self.descripcion_producto}"