from datetime import datetime
from django.db import models

class Author(models.Model):
  '''Object for book author'''

  first_name = models.CharField(max_length=128)
  last_name = models.CharField(max_length=128)

  def __unicode__(self):
    return self.last_name + ", " + self.first_name


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
