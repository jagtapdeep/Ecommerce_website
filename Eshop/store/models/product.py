from django.db import models
from .category import Category , SubCategory
from django.utils import timezone
from datetime import date

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,default='')
    images = models.ImageField(upload_to='uploads/products',default=None,null=False,blank=False)
    images1 = models.ImageField(upload_to='uploads/products',null=True,blank=True)
    images2 = models.ImageField(upload_to='uploads/products',null=True,blank=True)
    quantity = models.IntegerField(default=15)
    offer = models.IntegerField(default=0)
    rating = models.DecimalField(default=0,decimal_places=1,max_digits=5)
    review_count = models.IntegerField(default=0)
    brand = models.CharField(max_length=200,default='YWC')
    one_day_offer = models.BooleanField(default=False)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.name