from django.db import models

# Create your models here.
class File(models.Model):
    #a model to store our files in our table of a db
    id = models.AutoField(primary_key=True)
    Description=models.CharField(max_length=100)
    keywords= models.CharField(max_length=100)
    location = models.URLField(max_length=200)

