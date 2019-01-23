from django.db import models
from django.utils import timezone

class Victim(models.Model):
    phone_number = models.IntegerField()
    reported_date = models.DateTimeField(default = timezone.now)
    lat = models.DecimalField(max_digits=10,decimal_places=6)
    lon = models.DecimalField(max_digits=10,decimal_places=6)
    rescued = models.BooleanField(default=False)

    def setRescued(self, val):
        self.rescued = val

    def __str__(self):
        return str(self.id)

class Volunteer(models.Model):
    phone_number = models.IntegerField()
    reported_date = models.DateTimeField(default = timezone.now)
    lat = models.DecimalField(max_digits=10,decimal_places=6)
    lon = models.DecimalField(max_digits=10,decimal_places=6)
    location = models.TextField(max_length=100)

    def __str__(self):
        return str(self.id)