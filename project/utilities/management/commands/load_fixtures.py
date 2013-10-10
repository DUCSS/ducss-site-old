import os
import glob
from django.core.management.base import BaseCommand
from django.conf import settings
from django.core import management

def load_fixtures(app_name, fixture_dir_name):
    module = __import__(app_name)
    fixtures_dir = os.path.join(os.path.dirname(module.__file__), fixture_dir_name)
    if os.path.exists(fixtures_dir):
        filenames = glob.glob(os.path.join(fixtures_dir, '*.json'))
        filenames.sort()
        management.call_command('loaddata', *filenames)


class Command(BaseCommand):
    args = "<app_name1, app_name2, ...>"
    help = "Load fixtures in the named apps. The app's 'fixtures' directory will be searched. In DEBUG mode, the 'fixtures_dev' directory will also be searched. Fixtures will be loaded in filename order."

    def handle(self, *args, **options):
        for app_name in args:
            # Check that the app is one of our own, not a 3rd party app.
            if settings.DIRNAME in __import__(app_name).__file__:
                load_fixtures(app_name, 'fixtures')
                if settings.DEVELOPMENT_MODE:
                    load_fixtures(app_name, 'fixtures_dev')
