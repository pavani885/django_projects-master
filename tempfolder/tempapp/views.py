from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def home(request):
    return HttpResponse("Hi This is home page")
def firstpage(request):
    return HttpResponse("This is First page")
def secondpage(request):
    return HttpResponse("This is Second page")
def htmlpage(request):
    template = loader.get_template('student.html')
    return HttpResponse(template.render())
