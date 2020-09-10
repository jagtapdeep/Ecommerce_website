from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    subcategory = models.ForeignKey(Category, on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.name