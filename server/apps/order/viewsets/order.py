from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework import mixins

from apps.api.permissions.is_owner import IsOwnerOrReadOnly
from apps.order.models import OrderComment, Order
from apps.order.serializers.order import OrderCommentSerializer, OrderSerializer
from apps.cart.models.models import Cart
from apps.finance.models.models import DollarValue


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        print('!!!!!!!!!!', serializer.validated_data)
        cart = Cart.objects.filter(profile=self.request.user.profile).last()
        usd_price = DollarValue.objects.last().value
        # price =
        serializer.save(
            profile=self.request.user.profile,
            cart=cart,
            byn_price=usd_price * serializer.validated_data[''])


class OrderCommentViewSet(viewsets.ModelViewSet):
    serializer_class = OrderCommentSerializer
    queryset = OrderComment.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)
