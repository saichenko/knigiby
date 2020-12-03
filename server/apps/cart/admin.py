from django.contrib import admin

from .models import Cart


class CartAdmin(admin.ModelAdmin):
    readonly_fields = ('profile', )


admin.site.register(Cart, CartAdmin)
