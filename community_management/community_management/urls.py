"""
URL configuration for community_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from operator import index
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def welcome(request):
    return render(request, 'welcome.html')

def intro(request):
    return render(request, 'intro.html')


urlpatterns = [
    # path('admin/', admin.site.urls),

    # 首页
    path('', welcome, name='welcome'),

    # 关于我们
    path('intro/', intro, name='intro'),

    # deng登录
    path('login/', include('login.urls')),

    # 主页
    path('index/', include('index.urls')),

    # 地址管理
    path('address/', include('address.urls')),

    # 居民管理
    path('residents/', include('residents.urls')),

    # 物业管理
    path('properties/', include('properties.urls')),

    # 商户管理
    path('merchants/', include('merchants.urls')),

    # 个人信息
    path('profile/', include('admins.urls')),

]
