from events.models import Event

from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request, template=None):
	'''Home page'''
	context = RequestContext(request)

	context['events'] = Event.objects.all()

	return render_to_response(template, context_instance=context)

