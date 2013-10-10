import os
from django.core.management.base import NoArgsCommand
from django.conf import settings

class Command(NoArgsCommand):
    help = "Deletes old .pyc files in the project directory."

    def handle(self, *args, **options):
        for root, _, files in os.walk(settings.DIRNAME, topdown=False):
            files = filter(lambda filename: filename.endswith('.pyc'), files)
            for name in files:
                os.remove(os.path.join(root, name))
