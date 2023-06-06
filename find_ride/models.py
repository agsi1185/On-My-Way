from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class find_ride(models.Model):
    origin = models.CharField(max_length=150)
    destination = models.CharField(max_length=150)
    seats_req = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])

    def __str__(self):
        return self.origin