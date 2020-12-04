from rest_framework import serializers

from apps.products.models.products import Product, ProductImage, ProductComment


class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = ('id', 'product', 'profile', 'rate', 'text', 'created',)
        extra_kwargs = {
            'profile': {'read_only': True},
        }


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'product', 'image')


class ProductSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    genres = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    book_series = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    publisher = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    image = ProductImageSerializer(many=True, read_only=True)
    product_comment = ProductCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'authors', 'main_img', 'image', 'usd_price', 'genres', 'book_series', 'publisher',
            'published', 'pages_number', 'cover', 'format', 'isbn', 'weight_gr', 'age_restriction', 'books_available',
            'rating', 'product_comment'
        )
