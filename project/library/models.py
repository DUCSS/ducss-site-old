from datetime import datetime
from django.db import models
import re

class Author(models.Model):
  '''Object for book author'''

  first_name = models.CharField(max_length=128)
  last_name = models.CharField(max_length=128)

  @classmethod
  def create_from_csv(cls, author_lf):
      name = re.split(',',author_lf)
      first = name[1]
      surname = name[0]
      author = Author.objects.all().filter(first_name=first, last_name = surname)
      if len(author) == 0:
          author = cls(first_name=first, last_name=surname)
          author.save()
          author = Author.objects.all().filter(first_name=first, last_name = surname)
      return author

  def __unicode__(self):
    return self.first_name + " " + self.last_name 


class Book(models.Model):
  '''Object for library books'''
  IN = 0
  OUT = 1
  MISSING = 2
  REFERENCE = 3

  STATUS_CHOICES = (
      (IN, 'In'),
      (OUT, 'Out'),
      (MISSING, 'Missing'),
      (REFERENCE, 'This is a reference book and cannot be checked out')
  )


  title = models.CharField(max_length=128)
  isbn = models.CharField(max_length=13, blank=True, null=True)
  isbn13 = models.CharField(max_length=13, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  authors = models.ManyToManyField(Author)
  year_published = models.SmallIntegerField(blank=True, null=True)
  status = models.SmallIntegerField(default=IN, max_length=2, choices=STATUS_CHOICES)

  def __unicode__(self):
    return self.title


class Reservation(models.Model):
  '''Object for book reservations'''

  book_id = models.ForeignKey('Book')
  member_name = models.CharField(max_length=128)
  email = models.EmailField()
  date_created = models.DateTimeField(default=datetime.now())

  def __unicode__(self):
    return self.member_name + ": " + str(self.book_id)
