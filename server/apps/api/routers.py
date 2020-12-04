from rest_framework import routers

from apps.cart.viewsets.cart import CartApiView
from apps.order.viewsets.order import OrderCommentViewSet, OrderViewSet
from apps.products.viewsets.product import ProductViewSet, ProductCommentViewSet
from apps.secondary_objects.viewsets.address import AdressViewSet, StreetViewSet
from apps.secondary_objects.viewsets.for_books import GenreViewSet, BookSeriesViewSet, PublisherViewSet, AuthorViewSet
from apps.test.viewsets import TestViewSet
from apps.users.viewsets.users import UserViewSet

router = routers.DefaultRouter()
router.register('test', TestViewSet, basename='test')
router.register('user', UserViewSet, basename='user')
router.register('address', AdressViewSet, basename='address')
router.register('street', StreetViewSet, basename='street')
router.register('product', ProductViewSet, basename='product')
router.register('product-comment', ProductCommentViewSet, basename='product-comment')
router.register('cart', CartApiView, basename='cart')
router.register('order', OrderViewSet, basename='order')
router.register('genre', GenreViewSet, basename='genre')
router.register('bookseries', BookSeriesViewSet, basename='bookseries')
router.register('publisher', PublisherViewSet, basename='publisher')
router.register('author', AuthorViewSet, basename='author')
router.register('order-comment', OrderCommentViewSet, basename='order-comment')
