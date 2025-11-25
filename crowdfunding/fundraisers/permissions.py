from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    # Only the owner of a fundraiser can update or delete it.
    # Read-only requests are allowed for anyone.

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
    
class IsSupporterOrReadOnly(permissions.BasePermission):
    # Only the supporter (creator) of a pledge can update or delete it.
    # Read-only requests are allowed for anyone.
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.supporter == request.user