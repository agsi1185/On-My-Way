# Generated by Django 4.2.1 on 2023-06-06 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_ride', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_ride',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='new_ride',
            name='longitude',
        ),
    ]
