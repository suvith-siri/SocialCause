from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Datas(models.Model):
    name=models.CharField(max_length=100)
    don=models.CharField(max_length=100)
    phn=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    pic=models.ImageField(upload_to='pics') 
 