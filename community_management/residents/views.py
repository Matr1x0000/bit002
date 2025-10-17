from django.shortcuts import render

# Create your views here.
def residents(request):
    return render(request, 'residents/residents.html')

