import uuid
from django.db import models
from django.utils import timezone


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(unique=True)
    description   = models.TextField(blank=True, null=True)
    featured = models.CharField(
        max_length=20, 
        default='false',
        choices=[
            ('false', 'Fales'),
            ('true', 'True'),
        ])
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    read_time = models.CharField(max_length=255, blank=True, null=True)
    created_at  = models.DateTimeField(default=timezone.now)
    updated_at    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created_at',)


