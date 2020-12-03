from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.api.permissions.is_owner import IsOwner
from apps.secondary_objects.models.locational import Address
from apps.secondary_objects.serializers.address import AddressSerializer


class AdressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = (IsAuthenticated, IsOwner,)

    def filter_queryset(self, queryset):
        return queryset.filter(profile=self.request.user.profile)

    def create(self, request, *args, **kwargs):
        if self.request.user.profile.address.count() >= 2:
            raise ValidationError('You can not add more than 2 addresses.')
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(profile=(self.request.user.profile,))
