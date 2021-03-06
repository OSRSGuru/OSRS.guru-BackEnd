from django.db import models

# Create your models here.


class ServerLocation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"ServerLocation: {self.name}"


class Server(models.Model):
    world_id = models.IntegerField(primary_key=True)
    location = models.ForeignKey(ServerLocation, models.SET_NULL, blank=True, null=True, related_name="servers")
    members = models.BooleanField(blank=True, null=True, default=False)
    activity = models.CharField(max_length=255, blank=True, null=True)
    pvp = models.BooleanField(blank=True, null=True, default=False)
    high_risk = models.BooleanField(blank=True, null=True, default=False)
    leagues = models.BooleanField(blank=True, null=True, default=False)
    deadman = models.BooleanField(blank=True, null=True, default=False)
    skill_total = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Server: {self.world_id}"


class GameObject(models.Model):
    object_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"GameObject: {self.name}"
