from django.db import models

# Create your models here.
class todoapp(models.Model):
    notes=models.CharField(max_length=100)
    main=models.CharField(max_length=50)