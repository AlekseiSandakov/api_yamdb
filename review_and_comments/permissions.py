from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class ReviewCommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            and request.user.is_anonymous
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'DELETE']:
            return (
                obj.author == request.user
                or request.user.role in [request.user.ROLE_ADMIN,
                                         request.user.ROLE_MODERATOR]
            )
        return True
