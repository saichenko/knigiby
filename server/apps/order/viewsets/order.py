from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.api.permissions.is_owner import IsOwnerOrReadOnly
from apps.cart.models.models import Cart
from apps.finance.models.models import DollarValue
from apps.order.models.models import OrderComment, Order
from apps.order.serializers.order import OrderCommentSerializer, OrderSerializer


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def filter_queryset(self, queryset):
        return queryset.filter(profile=self.request.user.profile)

    def perform_create(self, serializer):
        cart = Cart.objects.filter(profile=self.request.user.profile).last()
        usd_price = DollarValue.objects.last().value
        serializer.save(
            cart=cart,
            profile=self.request.user.profile,
            receiving_method=serializer.validated_data['receiving_method'],
            byn_price=usd_price * cart.price_sum,
        )
        Cart.objects.create(profile=self.request.user.profile)


class OrderCommentViewSet(viewsets.ModelViewSet):
    serializer_class = OrderCommentSerializer
    queryset = OrderComment.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)
