from django.db import models

# Create your models here.
class Items(models.Model):
    title=models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    myfile=models.FileField(editable=False)



