
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Permiso personalizado: permite acceso de solo lectura a cualquiera,
    pero solo los administradores (staff) pueden escribir (crear, editar, borrar).
    """
    def has_permission(self, request, view):
        # Si el método es seguro (GET, HEAD, OPTIONS), permite el acceso.
        if request.method in SAFE_METHODS:
            return True
        # De lo contrario, solo permite el acceso si el usuario es staff.
        return request.user and request.user.is_staff