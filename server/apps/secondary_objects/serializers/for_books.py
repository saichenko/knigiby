from rest_framework.serializers import ModelSerializer

from apps.secondary_objects.models.for_books import Genre, BookSeries, Publisher, Author


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'description',)


class BookSeriesSerializer(ModelSerializer):
    class Meta:
        model = BookSeries
        fields = ('id', 'name', 'description')


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'description',)


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'description', 'image',)
