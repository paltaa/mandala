from django.db import models

class Programa(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    short = models.CharField(max_length=255)
    img = models.ImageField(upload_to="static/uploads")
    body = models.TextField(max_length=None)
    tag =  models.CharField(max_length=255)
# Create your models here.
    def __str__(self):
        return self.title
