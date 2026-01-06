from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """
    Allow read-only access to everyone,
    but write access only to the author.
    """

    def has_object_permission(self, request, view, obj):
        
        # Read permissions are allowed for any request
        if request.method in SAFE_METHODS:
            return True
        
        # Write permissions are allowed for author
        return obj.author == request.user