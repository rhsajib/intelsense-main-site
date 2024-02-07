# Generated by Django 4.2 on 2024-02-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0003_info_delete_career_delete_internship_delete_vacancy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='info_type',
            field=models.CharField(choices=[('career', 'Career'), ('internship', 'Internship'), ('vacancy', 'Vacancy')], default='career', max_length=30, unique=True),
        ),
    ]