from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('events',
    url(r'^all$',
        view='views.listing',
        kwargs={'template':'listing.html'},
        name='listing'
    ),
    url(r'(\s+)$',
    	view='views.event',
    	kwargs={'template':'event.html'},
    	name='event'
    )
)