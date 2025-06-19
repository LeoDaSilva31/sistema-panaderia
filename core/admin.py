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

# ---- Personalización para PRODUCTO ----
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_unitario')
    search_fields = ('nombre',)

# ---- Personalización para VENDEDOR ----
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni', 'telefono', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre', 'dni')

# ---- Personalización para ENTREGA (con inlines) ----
class DetalleEntregaInline(admin.TabularInline):
    model = DetalleEntrega
    extra = 1

class EntregaAdmin(admin.ModelAdmin):
    list_display = ('vendedor', 'fecha_entrega')
    list_filter = ('vendedor', 'fecha_entrega')
    inlines = [DetalleEntregaInline]
    readonly_fields = ('fecha_entrega',)

# ---- Personalización para COMPRA (con inlines) ----
class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra
    extra = 1

class CompraAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'fecha_compra', 'total_calculado')
    list_filter = ('fecha_compra', 'proveedor')
    inlines = [DetalleCompraInline]
    
# ---- Personalización para PAGO ----
class PagoAdmin(admin.ModelAdmin):
    list_display = ('vendedor', 'monto', 'metodo', 'fecha_pago')
    list_filter = ('vendedor', 'metodo', 'fecha_pago')


# ---- REGISTRO DE MODELOS Y SUS PERSONALIZACIONES ----
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(Entrega, EntregaAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Pago, PagoAdmin)
