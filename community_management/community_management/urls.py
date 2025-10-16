"""
URL configuration for community_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import render


# 首页视图
def home(request):
    # 渲染欢迎页面
    return render(request, 'welcome.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    # 居民管理相关
    path('residents/', include('residents.urls')),
    path('deceased/', include('deceased.urls')),
    path('disabled/', include('disabled.urls')),
    path('five_guarantees/', include('five_guarantees.urls')),
    path('low_income/', include('low_income.urls')),
    path('special_needs/', include('special_needs.urls')),
    path('special_objects/', include('special_objects.urls')),

    # 房产管理相关
    path('groups/', include('groups.urls')),
    path('buildings/', include('buildings.urls')),
    path('house/', include('house.urls')),
    path('units/', include('units.urls')),
    path('apartments/', include('apartments.urls')),
    path('communities/', include('communities.urls')),
    path('bungalows/', include('bungalows.urls')),
    path('hutong/', include('hutong.urls')),

    # 物业管理相关
    path('properties/', include('properties.urls')),
    path('property/', include('property.urls')),

    # 商户管理相关
    path('merchants/', include('merchants.urls')),
    path('streets/', include('streets.urls')),

    # 系统管理相关
    path('admins/', include('admins.urls')),
    path('auth/', include('authentication.urls')),
]
