import uuid
from django.db import models
from django.utils import timezone


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    statement = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    input = models.TextField(blank=True, null=True)
    output = models.TextField(blank=True, null=True)
    service_rating = models.CharField(
        max_length=20, 
        default='none',
        choices=[
            ('none', 'None'),
            ('top', 'Top'),
        ])
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProvidedService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    statement = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    services = models.ManyToManyField(Service, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        service_names = [s.name for s in self.services.all()]
        return f'Provided Services: {", ".join(service_names)}'

