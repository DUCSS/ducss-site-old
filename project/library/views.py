import datetime

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from library.models import Book
from library.models import Reservation
from library.forms import ReservationForm

def listing(request, template=None):
    '''Lists all the libraries books'''
    context = RequestContext(request)

    context['books'] = Book.objects.all().prefetch_related("authors")

    context['books_listing_page'] = True
    return render_to_response(template, context_instance=context)

def book(request, id, template=None):
    '''Full details for an book'''
    context = RequestContext(request)

    book = get_object_or_404(Book, pk=id)

    context['book'] = book
    context['book_page'] = True
    return render_to_response(template, context_instance=context)

def reserve(request, id, template=None):
    '''Reserve a book in the library'''
    context = RequestContext(request)
    book = get_object_or_404(Book, pk=id)
    if book.status == book.IN:
      if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid() and book.status == book.IN :
          reservation = form.save(commit=False)
          reservation.book_id = book
          reservation.save()
          book.status = book.OUT
          book.save()
          return redirect('library.views.book', id=id)
        else:
          context['reserve_form'] = form
          return render_to_response(template, context_instance=context)
      else:
        context['reserve_form'] = ReservationForm()
        context['book'] = book
        return render_to_response(template, context_instance=context)
    else:
      return redirect('library.views.book', id=id)
