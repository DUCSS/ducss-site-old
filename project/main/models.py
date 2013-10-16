from django.db import models

class Service(models.Model):
	'''Descriptions about services that the society provides'''

	title = models.CharField(max_length=128)
	description = models.TextField()
	image = models.ImageField(upload_to='services')

	def __unicode__(self):
		return self.title