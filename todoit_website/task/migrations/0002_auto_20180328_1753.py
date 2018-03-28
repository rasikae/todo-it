# Generated by Django 2.0.3 on 2018-03-28 21:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='iD',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='task',
            name='iD',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='task',
            name='progress',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
