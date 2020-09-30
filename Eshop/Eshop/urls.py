"""Eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static
from store import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('changepass/',views.changepass,name='changepass1'),
    path('changepass1',views.changepass1,name='changepass2'),
    path('addtocart/<int:id>',views.addtocart,name='addtocart'),
    path('search/',views.search,name='search'),
    path('order/<int:id>',views.order,name='order'),
    path('orders/',views.orders,name='orders'),
    path('top_offer/',views.top_offer,name='top_offer'),
    path('best_battery/',views.best_battery,name='best_battery'),
    path('top_rated/',views.top_rated,name='top_rated'),
    path('buyquantity/<int:id>',views.buyquantity,name='buyquantity'),
    path('onlinebuy/',views.onlinebuy,name='onlinebuy'),
    path('addcategory/',views.addcategory,name='addcategory'),
    path('addsubcategory/',views.addsubcategory,name='addsubcategory'),
    path('addproduct/',views.addproduct,name='addproduct'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
