from django.db import models
from .product import Product
from django.contrib.auth.models import User


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    user_name = models.CharField(max_length=50,default='guest')
    rating = models.DecimalField(decimal_places=1,max_digits=5)
    comments = models.CharField(max_length=100)    