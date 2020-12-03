from django.contrib import admin

from apps.products.models.products import Product, ProductImage, ProductComment


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductCommentInline(admin.TabularInline):
    model = ProductComment


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'last_modified',)
    inlines = (
        ProductImageInline,
        ProductCommentInline
    )


admin.site.register(Product, ProductAdmin)
