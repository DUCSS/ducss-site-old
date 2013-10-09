
from django.conf.urls import patterns, include, url
from django.contrib import admin

from mezzanine.core.views import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',

    # Admin Control Panel URL
    url(r'^admin/', include(admin.site.urls)),

    # Custom Modules URLs
    url(r'^$',
        view='theme.views.home',
        kwargs={'template':'base/home.html'},
        name='home'
    ),
    (r'^events/', include('events.urls', namespace='events', app_name='events')),
    
    # MEZZANINE'S URLS
    # ----------------
    # ADD YOUR OWN URLPATTERNS *ABOVE* THE LINE BELOW.
    # ``mezzanine.urls`` INCLUDES A *CATCH ALL* PATTERN
    # FOR PAGES, SO URLPATTERNS ADDED BELOW ``mezzanine.urls``
    # WILL NEVER BE MATCHED!

    # If you'd like more granular control over the patterns in
    # ``mezzanine.urls``, go right ahead and take the parts you want
    # from it, and use them directly below instead of using
    # ``mezzanine.urls``.
    ("^", include("mezzanine.urls")),
)

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = 'mezzanine.core.views.page_not_found'
handler500 = 'mezzanine.core.views.server_error'
