from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def service_details(request):
    return render(request, 'service-details.html')
def sd(request):
    return render(request, 'sd.html')
def ser(request):
    return render(request, 'ser.html')