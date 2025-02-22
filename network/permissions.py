from rest_framework import permissions


class IsActiveEmployee(permissions.BasePermission):
    """Проверка активности сотрудника."""
    def has_permission(self, request, view):
        return request.user.is_active and request.user.is_authenticated and request.user.is_staff
