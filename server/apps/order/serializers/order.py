from rest_framework.serializers import ModelSerializer

from apps.cart.serializers.cart import CartSerializer
from apps.order.models.models import Order, OrderComment


class OrderSerializer(ModelSerializer):
    cart = CartSerializer(many=False, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'cart', 'profile', 'receiving_method', 'status', 'byn_price', 'created', 'last_modified')
        extra_kwargs = {
            'profile': {'read_only': True},
            'cart': {'read_only': True},
            'status': {'read_only': True},
            'byn_price': {'read_only': True},
        }


class OrderCommentSerializer(ModelSerializer):
    class Meta:
        model = OrderComment
        fields = ('order', 'profile', 'text', 'created', 'last_modified')
        extra_kwargs = {'profile': {'read_only': True}}
