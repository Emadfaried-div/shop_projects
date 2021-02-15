from django.db import models
from django.utils.timezone import datetime

# Create your models here.

class Product(models.Model):
    PRDName=models.CharField(max_length=100)
    #category=models.ForeignKey()
    PRDDesc=models.TextField()
    PRDPrice=models.DecimalField(max_digits=5 ,decimal_places=2)
    PRDCost=models.DecimalField(max_digits=5 ,decimal_places=2)
    PRDCreated=models.DateTimeField( )