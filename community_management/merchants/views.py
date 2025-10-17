from django.shortcuts import render

# Create your views here.
def merchants(request):
    return render(request, 'merchants/merchants.html')

