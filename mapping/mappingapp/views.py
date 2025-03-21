from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def home(request):
    return HttpResponse("Welcome to the home Page.")
def firstpage(request):
    return HttpResponse("The page 1 after the home Page.")
def secondpage(request):
    return HttpResponse("The page 2 after the page 1.")
def thirdpage(request):
    return HttpResponse("This is the third page after the second page.")
