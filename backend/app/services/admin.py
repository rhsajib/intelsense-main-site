from django.contrib import admin
from .models import Service, ProvidedService

admin.site.register(Service)
admin.site.register(ProvidedService)