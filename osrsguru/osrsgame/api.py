from rest_framework.viewsets import ModelViewSet

from .serializers import ServerSerializer, GeographicalLocationSerializer, GameObjectSerializer
from .models import Server, GeographicalLocation, GameObject

class ServerViewSet(ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class GeographicalLocationViewSet(ModelViewSet):
    queryset = GeographicalLocation.objects.all()
    serializer_class = GeographicalLocationSerializer

class GameObjectViewSet(ModelViewSet):
    queryset = GameObject.objects.all()
    serializer_class = GameObjectSerializer