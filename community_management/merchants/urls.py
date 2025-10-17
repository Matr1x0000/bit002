from django.urls import path
from .views import merchants

urlpatterns = [
    path('', merchants, name='merchants'),
]
