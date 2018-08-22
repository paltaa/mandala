from django.db import models

class Programa(models.Model):
    title = models.CharField(max_length=255)
    short = models.CharField(max_length=255)
    img = models.ImageField(upload_to="programas/static/programas")
    body= models.TextField(max_length=None)
    tag =  models.CharField(max_length=255)
# Create your models here.
