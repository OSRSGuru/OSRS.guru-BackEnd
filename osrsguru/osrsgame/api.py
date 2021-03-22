from rest_framework.viewsets import ModelViewSet

from .serializers import ServerSerializer, ServerLocationSerializer, GameObjectSerializer
from .models import Server, ServerLocation, GameObject

class ServerViewSet(ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class GeographicalLocationViewSet(ModelViewSet):
    queryset = ServerLocation.objects.all()
    serializer_class = ServerLocationSerializer

class GameObjectViewSet(ModelViewSet):
    queryset = GameObject.objects.all()
    serializer_class = GameObjectSerializer