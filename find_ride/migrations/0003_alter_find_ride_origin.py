# Generated by Django 4.2.1 on 2023-06-07 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_ride', '0002_alter_find_ride_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='find_ride',
            name='origin',
            field=models.CharField(max_length=150),
        ),
    ]