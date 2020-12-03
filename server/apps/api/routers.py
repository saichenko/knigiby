from rest_framework import routers

from apps.products.viewsets.product import ProductViewSet
from apps.secondary_objects.viewsets.address import AdressViewSet
from apps.secondary_objects.viewsets.for_books import GenreViewSet, BookSeriesViewSet, PublisherViewSet, AuthorViewSet
from apps.test.viewsets import TestViewSet
from apps.users.viewsets.users import UserViewSet

router = routers.DefaultRouter()
router.register('test', TestViewSet, basename='test')
router.register('user', UserViewSet, basename='user')
router.register('address', AdressViewSet, basename='address')
router.register('product', ProductViewSet, basename='product')
router.register('genre', GenreViewSet, basename='genre')
router.register('bookseries', BookSeriesViewSet, basename='bookseries')
router.register('publisher', PublisherViewSet, basename='publisher')
router.register('author', AuthorViewSet, basename='author')
