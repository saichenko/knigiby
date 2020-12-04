# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from apps.cart.models.models import Cart
# from apps.order.models import Order
#
#
# @api_view(['POST'])
# def make_order(request):
#     cart = Cart.objects.filter(profile=request.user.profile).last()
#     order = Order.objects.create(
#         profile=request.user.profile,
#         cart=cart,
#         receiving_method=request.data['receiving_method'],
#         byn_price=...
#     )
