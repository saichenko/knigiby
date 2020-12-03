from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.secondary_objects.models.for_books import Genre, BookSeries, Publisher, Author
from apps.secondary_objects.serializers.for_books import (
    GenreSerializer, BookSeriesSerializer, PublisherSerializer, AuthorSerializer
)


# TODO: Probably these views should be deleted.
class GenreViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class BookSeriesViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    serializer_class = BookSeriesSerializer
    queryset = BookSeries.objects.all()


class PublisherViewSet(mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


class AuthorViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
