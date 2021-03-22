from .models import Server, ServerLocation, GameObject
from rest_framework import serializers


class ServerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Server
        fields = '__all__'


class ServerLocationSerializer(serializers.HyperlinkedModelSerializer):

    servers = ServerSerializer(read_only=True, many=True)

    class Meta:
        model = ServerLocation
        fields = '__all__'


class GameObjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameObject
        fields = '__all__'
