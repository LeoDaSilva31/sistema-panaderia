from rest_framework import serializers
from .models import (
    Vendedor,
    Producto,
    Entrega,
    DetalleEntrega,
    Pago,
    Compra,
    DetalleCompra
)


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        # Excluimos el campo 'user' por ahora para no complicar la API
        fields = ['id', 'nombre', 'dni', 'telefono', 'activo']

# Serializer para los detalles, será usado DENTRO del de Entrega
class DetalleEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleEntrega
        fields = ['id', 'producto', 'cantidad', 'precio_unitario_congelado']

class EntregaSerializer(serializers.ModelSerializer):
    # Aquí está la astucia: le decimos que "anide" el serializer de detalles.
    # Leemos los detalles (read_only=True) y como son varios, ponemos many=True.
    detalles = DetalleEntregaSerializer(many=True, read_only=True)

    class Meta:
        model = Entrega
        fields = ['id', 'vendedor', 'fecha_entrega', 'detalles']

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

class DetalleCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCompra
        fields = ['id', 'descripcion_producto', 'cantidad', 'precio_unitario']

class CompraSerializer(serializers.ModelSerializer):
    detalles = DetalleCompraSerializer(many=True, read_only=True)
    class Meta:
        model = Compra
        fields = ['id', 'fecha_compra', 'proveedor', 'total_calculado', 'detalles']