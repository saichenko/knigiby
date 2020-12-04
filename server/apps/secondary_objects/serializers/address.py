from rest_framework import serializers

from apps.secondary_objects.models.locational import Address, Street


class AddressSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    street = serializers.PrimaryKeyRelatedField(queryset=Street.objects.all(), many=False, read_only=False)

    class Meta:
        model = Address
        fields = ('id', 'profile', 'street', 'house', 'apartment')
        extra_kwargs = {
            'profile': {'read_only': True},
        }


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('id', 'city', 'name')
