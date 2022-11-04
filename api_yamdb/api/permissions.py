from rest_framework import permissions


class IsAdminOnlyPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (obj.role == 'admin')