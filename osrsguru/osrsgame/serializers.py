from .models import Server, GeographicalLocation, GameObject
from rest_framework import serializers

class ServerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Server
        fields = '__all__'

class GeographicalLocationSerializer(serializers.HyperlinkedModelSerializer):

    servers = ServerSerializer(read_only=True, many=True)

    class Meta:
        model = GeographicalLocation
        fields = '__all__'

class GameObjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameObject
        fields = '__all__'