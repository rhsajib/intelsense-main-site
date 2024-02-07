# Generated by Django 4.2 on 2024-02-05 17:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('given_by', models.CharField(max_length=255)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('organization_name', models.CharField(blank=True, max_length=255, null=True)),
                ('organization_location', models.CharField(blank=True, max_length=255, null=True)),
                ('opinion', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='partners/opinions/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('statement', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='partners/organizations/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('opinions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.opinion')),
                ('organizations', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.organization')),
            ],
        ),
    ]