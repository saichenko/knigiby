from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """ It is used by Adress, """
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        return request.user.profile == obj.profile.all().first()


class IsOwnerOrReadOnly(permissions.BasePermission):
    """ It is used by Adress, """
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.profile == obj.profile.all().first()
