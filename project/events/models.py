import datetime

from django.db import models
from mezzanine.pages.models import Page

class Event(Page):
	'''Event listing object'''

	date = models.DateField()
	location = models.CharField(max_length=45)