from django.urls import path

from apps.cart.viewsets import views

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('remove_product/', views.remove_product, name='remove_product'),
]
