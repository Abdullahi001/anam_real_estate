from django.db import models

# Create your models here.
class Ourteam(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    number = models.CharField(max_length=200)

def __str__(self):
    return self.name
