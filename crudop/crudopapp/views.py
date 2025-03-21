from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from django.urls import reverse

def index(request):
    persons = Person.objects.all()
    return render(request, 'index.html', {'persons': persons})

def insert(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Person.objects.create(name=name, email=email, phone=phone)
        return redirect('index')
    return render(request, 'insert.html')

def update(request, id):
    person = get_object_or_404(Person, id=id)

    if request.method == "POST":
        person.name = request.POST.get('name', person.name)
        person.email = request.POST.get('email', person.email)
        person.phone = request.POST.get('phone', person.phone)
        person.save()
        return redirect(reverse('index'))  # Ensure 'index' is correctly named in urls.py
    return render(request, 'update.html', {'person': person})
def delete(request, id):
    person = get_object_or_404(Person, id=id)
    person.delete()
    return redirect('index')
