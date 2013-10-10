import hmac, hashlib
from datetime import datetime
from django.conf import settings

def static(request):
    ''' Add static URL to the context, including the revision number (if known) when not in DEBUG mode. '''
    if settings.DEBUG and settings.REVISION:
        static_url = u'%sv%s/' % (settings.STATIC_URL, settings.REVISION)
    else:
        static_url = settings.STATIC_URL
    return {'STATIC_URL': static_url}