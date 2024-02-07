import uuid
from django.db import models
from django.utils import timezone


class Invitation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=False)
    details = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='invitations/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Investor(models.Model):
    statement = models.TextField(blank=True, null=True)
    description   = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='investors/', blank=True, null=True)
    created_at  = models.DateTimeField(default=timezone.now)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.statement


