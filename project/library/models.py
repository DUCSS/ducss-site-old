from django.db import models

class Author(models.Model):
  '''Object for book author'''

  first_name = models.CharField(max_length=128)
  last_name = models.CharField(max_length=128)

  def __unicode__(self):
    return self.last_name + ", " + self.first_name


class Book(models.Model):
  '''Object for library books'''

  title = models.CharField(max_length=128)
  isbn = models.CharField(max_length=13)
  isbn13 = models.CharField(max_length=13)
  description = models.TextField()
  authors = models.ManyToManyField(Author)
  year_published = models.SmallIntegerField(null=True)
  status = models.TextField(default="In")

  def __unicode__(self):
    return self.title


class Reservation(models.Model):
  '''Object for book reservations'''

  book_id = models.ForeignKey('Book')
  member_name = models.CharField(max_length=128)
  date_created = models.DateTimeField()

  def __unicode__(self):
    return self.member_name + ":" + self.book_id
