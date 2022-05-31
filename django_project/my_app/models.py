
from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField() 
    description = models.TextField()


    def __str__(self):
        return self.name
