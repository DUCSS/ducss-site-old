import datetime

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

import babel

def get_iso_code():
    '''Get ISO language code'''
    return settings.DEFAULT_LANGUAGE_CODE

def get_locale(iso_code=get_iso_code()):
    return babel.Locale(iso_code)

def get_date_format():
    '''Returns the ISO date format'''
    return "yy-mm-dd"

def get_human_day(date):
    '''Creates an easily human readable date such as Today, Yesterday etc.'''
    today = datetime.date.today()
    if date == today:
        return _("Today")
    elif date == (today - datetime.timedelta(days=1)):
        return _("Yesterday")
    elif date == (today + datetime.timedelta(days=1)):
        return _("Tomorrow")
    elif date > (today - datetime.timedelta(days=6)) and date < today:
        # Return the name of the day.
        return babel.dates.format_date(date, 'EEEE', locale=get_iso_code())
    else:
        # Return the date.
        return babel.dates.format_date(date, format='long', locale=get_iso_code())
