import datetime

from django import template
from django.conf import settings
from django.core.urlresolvers import reverse

register = template.Library()

@register.filter(name='render_percent')
def render_percent(value, precision=None):
    ''' Return the floating point number 'value' expressed as a percentage,
        with the decimal precision specified by the integer 'arg'.
    '''
    if not value:
        return '0%'

    value = float(value) * 100
    # If the value is less than 1 percent and precision isn't specified, default to 1 decimal place (so that a non-zero)
    # fraction doesn't get rendered as zero.
    if not precision and 0 < value < 1:
        precision = 1
    if precision:
        percentage = round(value, int(precision))
        return '%s%%' % percentage
    else:
        return '%s%%' % int(round(value))
