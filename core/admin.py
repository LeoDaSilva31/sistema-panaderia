from django.contrib import admin
from .models import (
    Vendedor,
    Producto,
    Entrega,
    DetalleEntrega,
    Pago,
    Compra,
    DetalleCompra
)

# Registramos cada modelo para que aparezca en el panel de admin
admin.site.register(Vendedor)
admin.site.register(Producto)
admin.site.register(Entrega)
admin.site.register(DetalleEntrega)
admin.site.register(Pago)
admin.site.register(Compra)
admin.site.register(DetalleCompra)