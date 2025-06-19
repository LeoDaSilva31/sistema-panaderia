# Archivo: core/views.py (Completo, con la nueva modificación)

from rest_framework import viewsets
# NUEVO: Importamos más permisos
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsAdminOrReadOnly # NUEVO: Importamos nuestro permiso personalizado

# ... (imports de modelos y serializers)
from .models import Vendedor, Producto, Entrega, Pago, Compra
from .serializers import VendedorSerializer, ProductoSerializer, EntregaSerializer, PagoSerializer, CompraSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    # MODIFICADO: Aplicamos nuestra nueva regla.
    permission_classes = [IsAdminOrReadOnly]

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
    # MODIFICADO: Solo los administradores pueden gestionar vendedores.
    permission_classes = [IsAdminUser]

# Para los siguientes, por ahora, solo requerimos que el usuario esté logueado.
# En la próxima clase, haremos que un vendedor solo pueda ver sus propias cosas.
class EntregaViewSet(viewsets.ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer
    permission_classes = [IsAuthenticated]

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    # Las compras solo las puede gestionar el admin
    permission_classes = [IsAdminUser]