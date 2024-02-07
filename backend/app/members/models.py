import uuid
from django.db import models
from django.utils import timezone


class Member(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=150, blank=False)
    position   = models.CharField(max_length=255, blank=False)
    team =  models.CharField(
        max_length=20, 
        default='none',
        choices=[
            ('none', 'None'),
            ('leaders', 'Leaders'),
            ('engineering', 'Engineering'),
            ('research', 'Research'),
            ('design', 'Design'),
            ('operations', 'Operations'),
            ('business', 'Business'),
        ],
    )
    email       = models.EmailField(unique=True, blank=False)
    mobile      = models.IntegerField(unique=True, blank=False)
    details   = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='members/', blank=True, null=True)
    created_at  = models.DateTimeField(default=timezone.now)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Team(models.Model):
    team =  models.CharField(
        max_length=20, 
        default='none',
        unique=True,
        choices=[
            ('none', 'None'),
            ('leaders', 'Leaders'),
            ('engineering', 'Engineering'),
            ('research', 'Research'),
            ('design', 'Design'),
            ('operations', 'Operations'),
            ('business', 'Business'),
        ],
    )
    statement = models.TextField(blank=True, null=True)
    description   = models.TextField(blank=True, null=True)
    cover_photo = models.ImageField(upload_to='teams/', blank=True, null=True)
    created_at  = models.DateTimeField(default=timezone.now)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.team
