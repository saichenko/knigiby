from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """ It is used by Adress, """
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        return request.user.profile == obj.profile.all().first()
