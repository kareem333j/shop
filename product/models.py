from django.db import models
from datetime import datetime
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8,decimal_places=3)
    time = models.DateTimeField(default=datetime.now)
    # time = models.DateTimeField(default=datetime.now)
    amounts = models.IntegerField(default=0)
    x = [
        ('Electronics','Electronics'),
        ('Home','Home'),
        ('Clothes','Clothes')
    ]
    category = models.CharField(max_length=20,choices=x)
    image = models.ImageField(upload_to='products-photos/%y/%m/%d',default=0)
    
    def __str__(self):
        return self.name