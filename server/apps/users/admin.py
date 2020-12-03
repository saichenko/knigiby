from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from apps.order.models import Order
from apps.cart.models import Cart
from apps.users.models.profiles import Profile


class OrderInline(admin.TabularInline):
    model = Order
    can_delete = False


class CartInline(admin.TabularInline):
    model = Cart
    can_delete = False


class ProfileInline(admin.StackedInline):
    inlines = (OrderInline, CartInline,)
    model = Profile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    # def get_country(self, instance):
    #     return instance.profile.address.city.country
    # get_country.short_description = 'Страна'

    # def get_city(self, instance):
    #     return instance.profile.address.city
    # get_city.short_description = 'Город'

    # def get_street_and_house(self, instance):
    #     return instance.profile.address.street_and_house
    # get_street_and_house.short_description = 'Улица и дом'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    inlines = (ProfileInline,)
    list_display = [
        'username', 'email', 'first_name', 'last_name', 'is_staff',
    ]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
