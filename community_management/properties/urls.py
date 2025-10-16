from django.urls import path
from .views import property_api

urlpatterns = [
    path('api/properties/', property_api, name='property_api'),
]