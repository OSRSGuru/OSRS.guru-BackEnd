import csv
from django.core.management import BaseCommand
from osrsgame.models import Server, ServerLocation

class Command(BaseCommand):
    help = 'Loads the ServerLocations CSV into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self,*args,**kwargs):

        Server.objects.all().delete() # Delete all objects

        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f)
            next(reader, None) # skip headers
            for row in reader:
                #print(row)
                world_id = row[0]
                server_location = row[1]
                model_server_location = ServerLocation.objects.filter(name=server_location)[0]
                members = row[3]
                activity = row[4]
                pvp = row[5]
                high_risk = row[6]
                leagues = row [7]
                deadman = row[8]
                skill_total = row[9]
                if skill_total == '':
                    skill_total = None

                mworld_id = Server.objects.get_or_create(world_id=world_id,
                                                         location=model_server_location,
                                                         members=members,
                                                         activity=activity,
                                                         pvp=pvp,
                                                         high_risk=high_risk,
                                                         leagues=leagues,
                                                         deadman=deadman,
                                                         skill_total=skill_total
                                                         )
