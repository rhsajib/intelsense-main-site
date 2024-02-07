import uuid
from django.db import models
from django.utils import timezone


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True, blank=False)
    statement     = models.TextField(blank=True, null=True)
    description   = models.TextField(blank=True, null=True)
    details   = models.TextField(blank=True, null=True)
    product_rating = models.CharField(
        max_length=20, 
        default='none',
        choices=[
            ('none', 'None'),
            ('top', 'Top'),
        ])
    logo = models.ImageField(upload_to='products/logos/', blank=True, null=True)
    video = models.FileField(upload_to='products/videos/', blank=True, null=True)
    product_url = models.URLField(blank=True, null=True)
    created_at  = models.DateTimeField(default=timezone.now)
    updated_at    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    


