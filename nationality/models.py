from django.db import models
from fighter.models import Fighter
# Create your models here.
class Nationality(models.Model):
    name = models.CharField(max_length=30)
    flag = models.ImageField(upload_to ='flags/')
    fighter = models.ForeignKey(Fighter, on_delete=models.CASCADE)
