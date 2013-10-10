import os
import sys

from django.core.management.base import NoArgsCommand
from django.conf import settings
from django.core import management

# Print ANSI escape sequences to get terminal colours.
# Makes it easier to see which app is currently being tested.
HEADER = '\033[95m'
ENDC = '\033[0m'

class Command(NoArgsCommand):
    help = "Runs test only in apps in this project."
    
    def handle(self, *args, **options):
        apps_to_test = []
        for app_name in settings.INSTALLED_APPS:
            app_dir = os.path.join(settings.DIRNAME, app_name)
            if os.path.exists(app_dir):
                apps_to_test.append(app_name)
                sys.stderr.write(HEADER + ('------ Testing: %s ------\n' % app_name) + ENDC)
        management.call_command('test', *apps_to_test)
