from django.urls import path
from .views import address_management, streets, groups, hutong, bungalows, communities, apartments, units, house_numbers

urlpatterns = [
    path('', address_management, name='address_management'),
    path('streets/', streets, name='streets'),
    path('groups/', groups, name='groups'),
    path('hutong/', hutong, name='hutong'),
    path('bungalows/', bungalows, name='bungalows'),
    path('communities/', communities, name='communities'),
    path('apartments/', apartments, name='apartments'),
    path('units/', units, name='units'),
    path('house_numbers/', house_numbers, name='house_numbers'),
]
