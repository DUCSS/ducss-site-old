from django.test import TestCase

class CleanTestCase(TestCase):
    def setUp(self):
    	# Warn the developer if the cache is enabled during testing
        from django.conf import settings
        dummy_backend = 'django.core.cache.backends.dummy.DummyCache'
        if settings.CACHES['default']['BACKEND'] != dummy_backend:
            print 'WARNING: Caching is enabled!. To disable caching during testing use the following caching backend:\n\t"%s"' % dummy_backend

