from rest_framework import serializers

from apps.products.models.products import Product


class ProductSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    genres = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    book_series = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    publisher = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Product
        fields = (
            'name', 'authors', 'main_img', 'usd_price', 'genres', 'book_series', 'publisher', 'published',
            'pages_number', 'cover', 'format', 'isbn', 'weight_gr', 'age_restriction', 'books_available', 'rating',
        )
