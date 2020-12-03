from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.products.serializers.product import ProductSerializer
from apps.products.models.products import Product


class ProductViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
