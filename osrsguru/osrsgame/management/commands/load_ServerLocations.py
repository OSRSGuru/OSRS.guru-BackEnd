import csv
from django.core.management import BaseCommand
from osrsgame.models import ServerLocation

class Command(BaseCommand):
    help = 'Loads the ServerLocations CSV into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self,*args,**kwargs):

        ServerLocation.objects.all().delete()  # Delete all objects

        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip headers
            for row in reader:
                server_location = ServerLocation.objects.get_or_create(name=row[1])
