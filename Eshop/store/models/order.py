from django.db import models
from .product import Product
from django.contrib.auth.models import User
import datetime


class Userorder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id = models.IntegerField(default=2)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100 ,default='')
    mobile = models.IntegerField()
    price = models.IntegerField()
    offer = models.IntegerField(default=0)
    pincode = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)