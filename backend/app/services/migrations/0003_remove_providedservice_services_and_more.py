# Generated by Django 4.2 on 2024-02-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_delete_topservice_remove_providedservice_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='providedservice',
            name='services',
        ),
        migrations.AddField(
            model_name='providedservice',
            name='services',
            field=models.ManyToManyField(blank=True, to='services.service'),
        ),
    ]
