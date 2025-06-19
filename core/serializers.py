# Archivo: core/serializers.py (Completo)

from rest_framework import serializers
from .models import Producto # Importamos el modelo que queremos "traducir"

# Creamos una clase para el traductor del Producto
# Hereda de ModelSerializer, que es una clase mágica de DRF
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto  # Le decimos: "El plano para la traducción es el modelo Producto"
        # Le decimos: "Traduce todos los campos que tiene el modelo"
        fields = '__all__'