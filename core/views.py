# Archivo: core/views.py (Completo)

from rest_framework import viewsets

# Importamos todos nuestros modelos y serializers
from .models import (
    Vendedor,
    Producto,
    Entrega,
    Pago,
    Compra
)
from .serializers import (
    VendedorSerializer,
    ProductoSerializer,
    EntregaSerializer,
    PagoSerializer,
    CompraSerializer
)


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

class EntregaViewSet(viewsets.ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer