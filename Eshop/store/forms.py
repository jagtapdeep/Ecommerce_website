from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models.order import Userorder 
from .models.review import Review
from .models.product import Product
from .models.category import Category ,SubCategory


class Signupform(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    password2 = forms.CharField(label='Re-password', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class Edituserform(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {'username':forms.TextInput(attrs={'class':'mb-4 px-3 in_con'}),'first_name':forms.TextInput(attrs={'class':'mb-4 px-3 in_con'}),'last_name':forms.TextInput(attrs={'class':'mb-4 px-3 in_con'}),'email':forms.EmailInput(attrs={'class':'mb-4 px-3 in_con'})}
        


class Userorderform(forms.ModelForm):
    class Meta:
        model = Userorder
        fields = ['quantity','address','pincode','mobile']
        widgets = {'quantity':forms.NumberInput(attrs={'class':'mb-4 px-3 in_con'}),'address':forms.TextInput(attrs={'class':'mb-4 px-3 in_con'}),'pincode':forms.NumberInput(attrs={'class':'mb-4 px-3 in_con'}),'mobile':forms.NumberInput(attrs={'class':'mb-4 px-3 in_con'})}


class Reviewform(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating','comments']
        widgets = {'rating':forms.NumberInput(attrs={'class':'in_con my-3 pl-2','placeholder':'Enter Rating'}),'comments':forms.TextInput(attrs={'class':'in_con my-3 pl-2','placeholder':'Enter Your Review'})}

class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','category','subcategory','images','images1','images2','price','quantity','offer','brand']

class Productcategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name':'Category Name'}
        error_messages = {'name':{'required':'Enter product category name.'}}

class Productsubcategory(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name','subcategory']
        labels = {'name':'Subcategory Name'}