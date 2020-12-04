from django.contrib import admin

from .models.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    readonly_fields = ('profile', 'price_sum')
