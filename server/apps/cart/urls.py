from django.urls import path

from apps.cart import views

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
]
