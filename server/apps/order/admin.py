from django.contrib import admin

from .models.models import Order, OrderComment


class OrderCommentInlineModelAdmin(admin.TabularInline):
    model = OrderComment


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('cart', 'profile')
    inlines = (OrderCommentInlineModelAdmin, )
