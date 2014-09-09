from django.contrib import admin

from library.models import Book
from library.models import Author
from library.models import Reservation

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Reservation)
