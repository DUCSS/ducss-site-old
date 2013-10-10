from django.core.management.base import NoArgsCommand
from django.conf import settings
from django.core import management

class Command(NoArgsCommand):
    help = "Runs syncdb, performs migrations, and loads fixtures."

    def handle(self, *args, **options):
        management.call_command('cleanpyc')
        management.call_command('syncdb')
        management.call_command('migrate')
        for app_name in settings.INSTALLED_APPS:
            management.call_command('load_fixtures', app_name)
