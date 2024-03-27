from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Addroom(models.Model):
    room = models.CharField(max_length=100)
    seats = models.IntegerField()
    details = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    image = models.FileField(upload_to='upload', null=True, default=True)

class Room(models.Model):
    room_number = models.CharField(max_length=50)

class Reservation(models.Model):
    roomm = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    reservation_timestop = models.TimeField()