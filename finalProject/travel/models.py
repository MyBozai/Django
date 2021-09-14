from django.db import models

# Create your models here.
class User(models.Model):
    choices = (
        (0,'male'),(1,'female')
    )
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex =  models.IntegerField(choices=choices,default=1)

class Search(models.Model):
    place = models.CharField(max_length=50)


class PlaceAddress(models.Model):
    address = models.CharField(max_length=255)
    infom = models.CharField(max_length=5000,default='无')

    def __str__(self):
        return self.address