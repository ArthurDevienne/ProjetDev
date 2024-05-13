from django.db import models

# Create your models here.
class Fighter(models.Model):
    firstName = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    profileImage = models.ImageField
    victoryNumber = models.IntegerField()
    defeatNumber = models.IntegerField()
    #nationality

