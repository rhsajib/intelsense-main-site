from django.contrib import admin
from .models import Invitation, Investor

admin.site.register(Investor)
admin.site.register(Invitation)