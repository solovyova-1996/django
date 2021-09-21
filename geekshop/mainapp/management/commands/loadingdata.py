from django.core.management.base import BaseCommand
from django.core import management
from django.core.management.commands import loaddata


class Command(BaseCommand):
    help = 'Loading data from file into database'

    def handle(self, *args, **kwargs):
        management.call_command(loaddata.Command(), 'dbp.json', verbosity=0)
