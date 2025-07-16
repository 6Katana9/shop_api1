from rest_framework.permissions import BasePermission


class IsAuthorOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return obj.customer == request.user
    
class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.customer