from django.contrib import admin

from library.models import Book
from library.models import Author
from library.models import Reservation
from library.models import Status

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Reservation)
admin.site.register(Status)
