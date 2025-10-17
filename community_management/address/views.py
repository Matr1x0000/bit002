from django.shortcuts import render

# Create your views here.

def address_management(request):
    return render(request, 'address/address_management.html')

def streets(request):
    return render(request, 'address/streets.html')

def groups(request):
    return render(request, 'address/groups.html')

def hutong(request):
    return render(request, 'address/hutong.html')

def bungalows(request):
    return render(request, 'address/bungalows.html')

def communities(request):
    return render(request, 'address/communities.html')

def apartments(request):
    return render(request, 'address/apartments.html')

def units(request):
    return render(request, 'address/units.html')

def house_numbers(request):
    return render(request, 'address/house_numbers.html')


