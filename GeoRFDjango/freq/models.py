#from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib import admin


# Create your models here.
class Frequency(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    range = models.CharField(max_length=10)
    power = models.CharField(max_length=10)
    upper = models.CharField(max_length=11)
    lower = models.CharField(max_length=12)
    user = models.CharField(max_length=50)

    class Meta:
        db_table = "frequencies"