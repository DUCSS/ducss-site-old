import datetime

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from events.models import Event

def listing(request, template=None):
    '''Lists all the upcoming events'''
    context = RequestContext(request)

    context['events'] = Event.objects.all().filter(date__gte=datetime.date.today())[:10]

    context['events_listing_page'] = True
    return render_to_response(template, context_instance=context)

def event(request, slug, template=None):
    '''Full details for an event'''
    context = RequestContext(request)

    event = get_object_or_404(Event, slug=slug)

    context['event'] = event
    context['event_page'] = True
    return render_to_response(template, context_instance=context)