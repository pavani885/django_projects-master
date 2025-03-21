

# Create your views here.
from django.shortcuts import render,redirect 
from.forms import login_form 
def login_view(request): 
    if request.method=='POST': 
        form=login_form(request.POST) 
        if form.is_valid():
            username=form.cleaned_data['username'] 
            password=form.cleaned_data['password'] 
            return render(request,'success.html',{'name':username}) 
    else: 
        form=login_form() 
    return render(request,'login.html',{'form':form})  
def show1(request): 
    return render(request,'success.html') 