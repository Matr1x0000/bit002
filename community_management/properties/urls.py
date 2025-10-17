from django.urls import path
from .views import property

urlpatterns = [
    path('', property, name='property'),
]
