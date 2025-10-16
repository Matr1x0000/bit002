from django.urls import path
from .views import business_api

urlpatterns = [
    path('', business_api, name='business_api'),
]