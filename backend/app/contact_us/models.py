import uuid
from django.db import models
from django.utils import timezone


class CustomerContact(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=150)
    email       = models.EmailField(unique=True, blank=False)
    mobile      = models.IntegerField(blank=True, null=True)
    message     = models.TextField(blank=True, null=True)
    created_at  = models.DateTimeField(default=timezone.now)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.email})'

