# Generated by Django 4.1.5 on 2023-01-30 19:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='datetime',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
