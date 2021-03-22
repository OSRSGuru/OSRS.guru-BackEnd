from django.contrib import admin

# Register your models here.

from .models import Server, ServerLocation, GameObject

admin.site.register(Server)
admin.site.register(ServerLocation)
admin.site.register(GameObject)