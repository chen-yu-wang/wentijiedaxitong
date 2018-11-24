"""BBSProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#_*_coding:utf-8_*_

from django.conf.urls import url
from django.contrib import admin
from BBS import views
from django.urls import path,include

urlpatterns = [
    url(r'^category/(\d+)/$',views.category,name="category" ),
    url(r'^article/(\d+)/$',views.article_detail,name="article_detail"),
    url(r'^article/new/$',views.new_article,name="new_article"),
    url(r'account/logout/',views.acc_logout,name='logout'),
    url(r'account/login/',views.acc_login,name='login'),
    url(r'categoryTime/(\d+)/$',views.categoryTime,name='categoryTime'),                         #新增
    url(r'categoryQuality/(\d+)/$',views.categoryQuality,name='categoryQuality'),               #新增
    url(r'categoryTime/(\d+)/getGood_num/(\d+)/',views.getGood_num,name='getGood_num'),        #新增
    url(r'categoryTime/(\d+)/getBad_num/(\d+)/', views.getBad_num, name='getBad_num'),         #新增
    url(r'categoryQuality/(\d+)/getGood_num1/(\d+)/',views.getGood_num1,name='getGood_num1'), #新增
    url(r'categoryQuality/(\d+)/getBad_num1/(\d+)/', views.getBad_num1, name='getBad_num1'),  #新增
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),


]
