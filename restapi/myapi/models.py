from django.db import models

# Create your models here.

class Coil(models.Model):
    heat = models.CharField(max_length=64)
    grade = models.CharField(max_length=64)


    def __str__(self):
        return self.name

