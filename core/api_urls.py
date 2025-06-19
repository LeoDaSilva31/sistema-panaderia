
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()

router.register(r'productos', views.ProductoViewSet, basename='producto')
router.register(r'vendedores', views.VendedorViewSet, basename='vendedor')
router.register(r'entregas', views.EntregaViewSet, basename='entrega')
router.register(r'pagos', views.PagoViewSet, basename='pago')
router.register(r'compras', views.CompraViewSet, basename='compra')

urlpatterns = [
    path('', include(router.urls)),
]