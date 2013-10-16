import datetime

from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404

from utilities.utils import create_form
from events.models import Event
from main.forms import ContactForm
from main.models import Service

def home(request, template=None):
    '''Home page'''
    context = RequestContext(request)

    contact_form = create_form(ContactForm, request)
    if request.method == "POST":
    	if contact_form.is_valid():
    		contact_form.save()
    		return HttpResponseRedirect(reverse('home'))

    context['events'] = Event.objects.all().filter(date__gte=datetime.date.today()).order_by('date')[:4]
    context['services'] = Service.objects.all()
    context['contact_form'] = contact_form

    context['home_page'] = True
    return render_to_response(template, context_instance=context)