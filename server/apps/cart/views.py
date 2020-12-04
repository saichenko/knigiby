from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.cart.models.models import Cart
from apps.products.models.products import Product


@api_view(['POST'])
def add_product(request):
    cart = Cart.objects.filter(profile=request.user.profile).last()
    cart.product.add(Product.objects.get(id=request.data['id']))
    return Response({'message': 'product successfully added to the cart.'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def remove_product(request):
    cart = Cart.objects.filter(profile=request.user.profile).last()
    cart.product.remove(Product.objects.get(id=request.data['id']))
    return Response({'message': 'product successfully removed from the cart.'}, status=status.HTTP_200_OK)
