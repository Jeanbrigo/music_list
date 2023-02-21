from django.db import models

class Song(models.Model):
    Title = models.CharField(max_length=100)
    Artist = models.CharField(max_length=100)
# Create your models here.
