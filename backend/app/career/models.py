import uuid
from django.db import models
from django.utils import timezone


class Opportunity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    introduction = models.TextField(blank=True, null=True)
    team =  models.CharField(
        max_length=30, 
        default='none',
        choices=[
            ('none', 'None'),
            ('business', 'Business'),
            ('design', 'Design'),
            ('engineering', 'Engineering'),
            ('ml', 'Machine Learning'),
            ('leaders', 'Leaders'),
            ('operations', 'Operations'),
            ('research', 'Research'),
        ],
    )

    job_type =  models.CharField(
        max_length=30, 
        default='none',
        choices=[
            ('job', 'Job'),
            ('internship', 'Internship'),
        ],
    )

    employment_type =  models.CharField(
        max_length=30, 
        default='none',
        choices=[
            ('full_time', 'Full-time'),
            ('part_time', 'Part-time'),
            ('contract', 'Contract'),
        ],
    )

    location = models.CharField(max_length=100)
    responsibilities = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    apply_instructions = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='career/opportunities/', blank=True, null=True)
    published_at = models.DateField(default=timezone.now)
    deadline = models.DateField()
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-published_at',)
        verbose_name_plural = 'Opportunities'

    def __str__(self):
        return self.title


class Info(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    info_type =  models.CharField(
        max_length=30, 
        default='career',
        unique=True,
        choices=[
            ('career', 'Career'),
            ('internship', 'Internship'),
            ('vacancy', 'Vacancy'),
        ],
    )
    statement = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image   = models.ImageField(upload_to='career/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.info_type
    
    class Meta:
        verbose_name_plural = 'Info'



