from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',
        view='main.views.home',
        kwargs={'template':'home.html'},
        name='home'
    ),
    (r'^library/', include('library.urls', namespace='library', app_name='library')),
    (r'^events/', include('events.urls', namespace='events', app_name='events')),
    url(r'^event/(?P<slug>[-\w]+)/$',
        view='events.views.event',
        kwargs={'template':'event.html'},
        name='event_clean'
    ),
    url(r'^library/book/(?P<id>[-\w]+)/$',
        view='library.views.book',
        kwargs={'template':'book.html'},
        name='book_clean'
    ),
    url(r'^library/book/(?P<id>[-\w]+)/reserve$',
        view='library.views.reserve',
        kwargs={'template':'library/reserve.html'},
        name='reserve_clean'
    ),
    (r'^/', include('main.urls', namespace='main', app_name='main')),
    url(r'^admin/', include(admin.site.urls))
)

# In debug mode, static files are automatically served by Django.
# Also serve user-uploaded files.
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s/(?P<path>.*)$' % settings.UPLOADS_DIRNAME,
            'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
            }
        ),
        url(r'^%(MEDIA_URL)s/(?P<path>.*)$' % {'MEDIA_URL': settings.MEDIA_URL.strip('/')},
            'django.views.static.serve',
            { 'document_root': settings.MEDIA_ROOT }),
   )
