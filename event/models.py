from django.db import models
from clients.models import Client
from fighter.models import Fighter
# Create your models here.

class Event(models.Model):
    eventDate = models.DateField()
    difficulty = models.IntegerField() # Will be linked to fighter indice strength
    place = models.CharField(max_length=30)
    banner = models.ImageField(upload_to ='banner/')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    fighter = models.ForeignKey(Fighter, on_delete=models.CASCADE)
