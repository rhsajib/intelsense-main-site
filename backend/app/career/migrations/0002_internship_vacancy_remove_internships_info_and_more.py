# Generated by Django 4.2 on 2024-02-07 18:58

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('statement', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('statement', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Vacancies',
            },
        ),
        migrations.RemoveField(
            model_name='internships',
            name='info',
        ),
        migrations.RemoveField(
            model_name='internships',
            name='opportunities',
        ),
        migrations.RemoveField(
            model_name='vacancies',
            name='info',
        ),
        migrations.RemoveField(
            model_name='vacancies',
            name='opportunities',
        ),
        migrations.AlterModelOptions(
            name='opportunity',
            options={'ordering': ('-published_at',), 'verbose_name_plural': 'Opportunities'},
        ),
        migrations.RenameField(
            model_name='opportunity',
            old_name='department',
            new_name='team',
        ),
        migrations.RemoveField(
            model_name='career',
            name='info',
        ),
        migrations.RemoveField(
            model_name='career',
            name='internships',
        ),
        migrations.RemoveField(
            model_name='career',
            name='vacancies',
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='type',
        ),
        migrations.AddField(
            model_name='career',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='statement',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='employment_type',
            field=models.CharField(choices=[('full_time', 'Full-time'), ('part_time', 'Part-time'), ('contract', 'Contract')], default='none', max_length=30),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='job_type',
            field=models.CharField(choices=[('job', 'Job'), ('internship', 'Internship')], default='none', max_length=30),
        ),
        migrations.AlterField(
            model_name='career',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Info',
        ),
        migrations.DeleteModel(
            name='Internships',
        ),
        migrations.DeleteModel(
            name='Vacancies',
        ),
    ]
