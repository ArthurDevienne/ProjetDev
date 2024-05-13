from django.db import models

#model 
class Client(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    birthDate = models.DateField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    profileImage = models.ImageField(upload_to ='clientImage/')
    def __str__(self):
        return f"{self.firstName} {self.lastName}"

