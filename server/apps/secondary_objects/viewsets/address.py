from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from url_filter.integrations.drf import DjangoFilterBackend

from apps.api.permissions.is_owner import IsOwner
from apps.secondary_objects.models.locational import Address, Street
from apps.secondary_objects.serializers.address import AddressSerializer, StreetSerializer


class AdressViewSet(viewsets.ModelViewSet):
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


class StreetViewSet(viewsets.GenericViewSet,
                    ListModelMixin):
    serializer_class = StreetSerializer
    queryset = Street.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('city',)
