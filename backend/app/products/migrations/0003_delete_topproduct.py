# Generated by Django 4.2 on 2024-02-07 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_delete_topproduct_topproduct'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TopProduct',
        ),
    ]
