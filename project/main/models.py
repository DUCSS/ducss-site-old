from django.db import models
from django_boto.s3.storage import S3Storage

s3 = S3Storage()

class Service(models.Model):
	'''Descriptions about services that the society provides'''

	title = models.CharField(max_length=128)
	description = models.TextField()
	image = models.ImageField(storage=s3, upload_to='uploads')

	def __unicode__(self):
		return self.title