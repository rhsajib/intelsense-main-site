# Generated by Django 4.2 on 2024-02-05 18:24

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TopService',
        ),
        migrations.RemoveField(
            model_name='providedservice',
            name='info',
        ),
        migrations.AddField(
            model_name='providedservice',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='providedservice',
            name='statement',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='providedservice',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='TopService',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.service')),
            ],
            bases=('services.service',),
            managers=[
                ('services', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='Info',
        ),
    ]