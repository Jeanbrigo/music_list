from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=99)
    artist = models.CharField(max_length=100)
# Create your models here.
