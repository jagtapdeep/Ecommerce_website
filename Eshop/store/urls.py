from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    # path('filter/',views.filter,name='filter')
    path('filter/<int:id>',views.filter,name='filter'),
    # path('userdetail/<int:id>',views.user_detail,name='userdetail')
    path('productview/<int:id>',views.productview,name='productview'),
    path('usercart/',views.user_cart,name='usercart'),
    path('search/',views.search,name='search'),   
    path('subfilter/<int:id>',views.subfilter,name='subfilter'), 
    path('delete/<int:id>',views.delete,name='delete'),  
    path('del_account/<int:id>',views.del_account,name='del_account'),  
]