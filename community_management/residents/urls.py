from django.urls import path
from .views import residents

urlpatterns = [
    path('', residents, name='residents'),
]
