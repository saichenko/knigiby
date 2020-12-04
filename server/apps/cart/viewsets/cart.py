from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.cart.models.models import Cart
from apps.cart.serializers.cart import CartSerializer


class CartApiView(ListModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get(self, request, format=None):
        cart = Cart.objects.filter(profile=request.user.profile).last()
        serializer = CartSerializer(cart)
        return Response(serializer.data)
