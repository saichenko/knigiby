from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN
from url_filter.integrations.drf import DjangoFilterBackend

from apps.api.permissions.is_owner import IsOwnerOrReadOnly
from apps.products.models.products import Product, ProductComment
from apps.products.serializers.product import ProductSerializer, ProductCommentSerializer


class ProductViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductCommentViewSet(viewsets.ModelViewSet):
    serializer_class = ProductCommentSerializer
    queryset = ProductComment.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('product',)

    def create(self, request, *args, **kwargs):
        if ProductComment.objects.filter(
                profile=request.user.profile,
                product_id=request.data['product']).exists():
            return Response({'message': 'you can not post more than 1 review.'}, status=HTTP_403_FORBIDDEN)
        return super().create(request)

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)
