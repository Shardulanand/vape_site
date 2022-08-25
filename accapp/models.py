from distutils.command.upload import upload
from pydoc import describe
from tokenize import Number
from django.db import models


class product(models.Model):
    name=models.CharField(max_length=250)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='product image/')

    
class reachus(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    PhoneNumber=models.FloatField()
    description=models.TextField()