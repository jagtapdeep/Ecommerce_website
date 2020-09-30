from django.contrib import admin
from .models.product import Product
from .models.category import Category , SubCategory
from .models.order import Userorder
from .models.review import Review

# Register your models here.
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name','price','description','quantity','offer','rating','review_count','brand','category','subcategory']

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(SubCategory)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Userorder)
class AdminUserorder(admin.ModelAdmin):
    list_display = ['id','product','customer','quantity','offer','price','date']

@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    list_display = ['id','product_id','customer_id','user_name','rating','comments']
