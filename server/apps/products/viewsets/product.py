from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.api.permissions.is_owner import IsOwnerOrReadOnly
from apps.products.models.products import Product, ProductComment
from apps.products.serializers.product import ProductSerializer, ProductCommentSerializer


class ProductViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# TODO: Add filtering by id
class ProductCommentViewSet(viewsets.ModelViewSet):
    serializer_class = ProductCommentSerializer
    queryset = ProductComment.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        return serializer.save(profile=self.request.user.profile)
