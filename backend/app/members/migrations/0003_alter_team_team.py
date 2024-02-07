# Generated by Django 4.2 on 2024-02-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_team_remove_design_info_remove_design_member_ptr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team',
            field=models.CharField(choices=[('none', 'None'), ('leaders', 'Leaders'), ('engineering', 'Engineering'), ('research', 'Research'), ('design', 'Design'), ('operations', 'Operations'), ('business', 'Business')], default='none', max_length=20, unique=True),
        ),
    ]
