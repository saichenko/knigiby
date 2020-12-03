from django.contrib import admin

from .models.for_books import Genre, BookSeries, Publisher, Author
from .models.locational import Country, City, Address, Street

admin.site.register(Genre)
admin.site.register(BookSeries)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Country)
admin.site.register(Street)
admin.site.register(City)
admin.site.register(Address)
