# Generated by Django 2.0.3 on 2018-04-02 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20180401_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
