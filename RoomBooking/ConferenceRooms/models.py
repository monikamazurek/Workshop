from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.IntegerField()
    projector = models.BooleanField(default=True)


class Reservation(models.Model):
    date = models.DateField(null=True)
    room_id = models.IntegerField(primary_key=True)
    comments = models.TextField()
    booking = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
