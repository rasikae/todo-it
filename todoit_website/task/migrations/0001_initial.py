# Generated by Django 2.0.3 on 2018-03-25 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('iD', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('due_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('iD', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('do_date', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('iD', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
