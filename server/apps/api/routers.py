from rest_framework import routers

from apps.test.viewsets import TestViewSet
from apps.users.viewsets.users import UserViewSet
from apps.secondary_objects.viewsets.address import AdressViewSet


router = routers.DefaultRouter()
router.register('test', TestViewSet, basename='test')
router.register('user', UserViewSet, basename='user')
router.register('address', AdressViewSet, basename='address')
