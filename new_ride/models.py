from django.db import models

# Create your models here.

class new_ride(models.Model):
    origin = models.CharField(max_length=150)
    destination = models.CharField(max_length = 150)
    seats_avail = models.IntegerField()

    def __str__(self):
        return self.destination