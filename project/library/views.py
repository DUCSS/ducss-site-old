import datetime

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from library.models import Book

def listing(request, template=None):
    '''Lists all the libraries books'''
    context = RequestContext(request)

    context['books'] = Book.objects.all()

    context['books_listing_page'] = True
    return render_to_response(template, context_instance=context)

def book(request, id, template=None):
    '''Full details for an book'''
    context = RequestContext(request)

    book = get_object_or_404(Book, pk=id)

    context['book'] = book
    context['book_page'] = True
    return render_to_response(template, context_instance=context)
