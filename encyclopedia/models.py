from django.db import models

# Create your models here.
class Items(models.Model):
    name=models.CharField(max_length=200)
    myfile=models.FileField()
