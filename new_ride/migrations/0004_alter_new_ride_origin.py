# Generated by Django 4.2.2 on 2023-06-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_ride', '0003_alter_new_ride_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_ride',
            name='origin',
            field=models.CharField(max_length=150),
        ),
    ]