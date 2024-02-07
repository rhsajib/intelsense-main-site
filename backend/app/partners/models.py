import uuid
from django.db import models
from django.utils import timezone


class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    statement = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='partners/organizations/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Opinion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    given_by = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, blank=True, null=True)
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    organization_location = models.CharField(max_length=255, blank=True, null=True)
    opinion = models.TextField()
    photo = models.ImageField(upload_to='partners/opinions/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Opinion by {self.given_by} from {self.organization_name}"


class Partner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organizations = models.ManyToManyField(Organization, blank=True)
    opinions = models.ManyToManyField(Opinion, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        partners = [s.name for s in self.organizations.all()]
        return f'Partners: {", ".join(partners)}'
