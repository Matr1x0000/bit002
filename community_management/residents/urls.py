from django.urls import path
from .views import resident_api

urlpatterns = [
    path('', resident_api, name='resident_api'),
]