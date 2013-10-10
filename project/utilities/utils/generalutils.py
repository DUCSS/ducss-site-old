import uuid

from django.contrib.sites.models import Site
from django.shortcuts import _get_queryset

def get_object_or_none(klass, *args, **kwargs):
    '''
    Uses get() to return an object, or None if the object
    does not exist.

    klass may be a Model, Manager, or QuerySet object. All other passed
    arguments and keyword arguments are used in the get() query.

    Note: Like with get(), an MultipleObjectsReturned will be raised if more than one
    object is found.

    Note: This function is based off django.shortcuts.get_object_or_404
    '''
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return None

def generate_uuid():
    ''' Generate random uuid
    Use uuid4 as recommended by
    http://docs.python.org/2/library/uuid.html '''
    return uuid.uuid4().hex[:16].upper()