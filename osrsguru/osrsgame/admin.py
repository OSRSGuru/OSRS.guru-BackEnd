from django.contrib import admin

# Register your models here.

from .models import Server, GeographicalLocation, GameObject

admin.site.register(Server)
admin.site.register(GeographicalLocation)
admin.site.register(GameObject)