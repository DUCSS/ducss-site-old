import logging
from django.test import TestCase

_logger = logging.getLogger(__name__)

class CleanTestCase(TestCase):
    def setUp(self):
        from utilities.utils.memoizeutils import invalidate_all_memoization
        _logger.debug("Invalidating memoized functions.")
        invalidate_all_memoization()

        from django.conf import settings
        dummy_backend = 'django.core.cache.backends.dummy.DummyCache'
        if settings.CACHES['default']['BACKEND'] != dummy_backend:
            _logger.warning('Caching is enabled!. To disable caching during testing use the following caching backend:\n\t"%s"' % dummy_backend)

