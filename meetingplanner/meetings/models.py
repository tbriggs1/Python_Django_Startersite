from datetime import time
from django.db import models

# Create your models here.

#Model Class called Room which represents a meeting room with room name, floor number and a room.
class Room(models.Model):
    room_name = models.CharField(max_length=100)
    floor_number = models.IntegerField(default=1)
    room_number = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.room_name}: room {self.floor_number}: on floor"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)

