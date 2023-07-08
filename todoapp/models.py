from django.db import models

# Create your models here.
class todoapp(models.Model):
    Dates=models.DateTimeField()
    Importancy= models.CharField(max_length=50)
    Notes = models.CharField(max_length=100)