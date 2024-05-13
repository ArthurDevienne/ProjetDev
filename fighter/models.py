from django.db import models

# Create your models here.
class Fighter(models.Model):
    firstName = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    profileImage = models.ImageField
    weight = models.IntegerField()
    height = models.IntegerField()
    victory = models.IntegerField()
    defeat = models.IntegerField()
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE)

