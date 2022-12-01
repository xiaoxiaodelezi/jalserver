from django.db import models

# Create your models here.

class Airport(models.Model):
    station=models.CharField(max_length=3)
    country=models.CharField(max_length=2)
    def __str__(self):
        return self.station