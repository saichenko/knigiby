from rest_framework import serializers

from apps.cart.models.models import Cart


class CartSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'profile', 'product',)
