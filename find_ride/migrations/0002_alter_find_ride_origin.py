# Generated by Django 4.2.1 on 2023-06-06 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_ride', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='find_ride',
            name='origin',
            field=models.CharField(help_text='Enter orgin', max_length=150),
        ),
    ]
