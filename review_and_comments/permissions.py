from rest_framework import permissions


class ReviewCommentPermission(permissions.BasePermission):
<<<<<<< HEAD
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                and request.user.is_anonymous
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'DELETE']:
            return (obj.author == request.user
                    or request.user.role in [request.user.ROLE_ADMIN,
                                             request.user.ROLE_MODERATOR])
        return True
=======
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return(
                obj.author == request.user
                or request.user.role in [request.user.ROLE_ADMIN,
                                         request.user.ROLE_MODERATOR]
            )
>>>>>>> 08549b4e8d21c23ff4223bbb065eaa23cac4e507
