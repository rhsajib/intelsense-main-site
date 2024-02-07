import uuid
from django.db import models
from django.utils import timezone


class AboutUs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic =  models.CharField(
        max_length=100, 
        unique=True,
        default='none',
        choices=[
            ('none', 'None'),
            ('who_we_are', 'Who we are'),
            ('what_we_do', 'What we do'),
            ('why_intelsense', 'Why Intelsense'),
            ('mission', 'Mission'),
            ('story', 'Story'),
        ],
    )
    statement = models.TextField(blank=True, null=True)
    reasons = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='about_us/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.topic


class Statement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    statement = models.TextField(unique=True)
    author = models.CharField(max_length=250,blank=True, null=True)
    author_photo = models.ImageField(upload_to='about_us/statements/authors/', blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='statements/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.statement


class Timeline(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year = models.IntegerField(unique=True)
    title = models.TextField(blank=True, null=True)
    statement = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='about_us/timeline/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.year)



