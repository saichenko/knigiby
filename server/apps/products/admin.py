from django.contrib import admin

from apps.products.models.products import Product, ProductImage, ProductComment


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductCommentInline(admin.TabularInline):
    model = ProductComment


@admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'last_modified', 'rating')
    inlines = (
        ProductImageInline,
        ProductCommentInline
    )
