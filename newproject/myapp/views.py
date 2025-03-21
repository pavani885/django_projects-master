from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def greet(request):
    return HttpResponse("This is new app to launch by 23b01a1249")
def myapp_home(request):
    return HttpResponse("Welcome to firstApp!")
