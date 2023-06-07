from django.db import models
import uuid
# Create your models here.

class new_ride(models.Model):
    origin = models.CharField(max_length=150)
    destination = models.CharField(max_length = 150)
    seats_avail = models.IntegerField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    
    def __str__(self):
        return self.origin