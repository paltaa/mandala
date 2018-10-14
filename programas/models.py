from django.db import models

class Programa(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    short = models.CharField(max_length=255)
    img = models.ImageField()
    body = models.TextField(max_length=None)
    coaching =  models.BooleanField(default=False )
    desarrollo = models.BooleanField(default=False)
    salud = models.BooleanField(default=False)
# Create your models here.
    def __str__(self):
        return self.title
