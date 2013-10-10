from django.db import models

class Event(models.Model):
	'''Object for planned events'''

	title = models.CharField(max_length=128)
	slug = models.SlugField()
	date = models.DateTimeField()
	location = models.CharField(max_length=128)
	description = models.TextField()

	def __unicode__(self):
		return self.title
