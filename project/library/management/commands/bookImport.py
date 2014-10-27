from django.core.management.base import BaseCommand, CommandError
from library.models import Book
from library.models import Author
import csv
import urllib2

class Command(BaseCommand):
    args = '<url>'
    help = 'Import csv file of books from url'

    def parse_csv(self, url):
        data = urllib2.urlopen(url)
        if data:
            self.save(data)
            return True
        return False

    def save(self, file_csv):
        records = csv.reader(file_csv)
        next(records)   # skip the first line
        for line in records:
            if len(line) == 7:
                title = line[0]
                author_lf = line[2]
                isbn = line[4] or None
                isbn13 = line[5]  or None
                yr_published = line[6] or None
                author = Author.create_from_csv(author_lf)
                book = Book(title=title, isbn=isbn, isbn13=isbn13, year_published=yr_published)
                book.save()
                book.authors = author
                book.save()

    def handle(self, *args, **options):
        for url in args:
          result = self.parse_csv(url)
          if result:
              print "Parsed CSV"
          else:
              print "Failed to parse"
