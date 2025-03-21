from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from faker import Faker
import random


def insert_rows(request):
    fake = Faker()
    for _ in range(50):
        Person.objects.create(
            name=fake.name(),
            age=random.randint(18, 80),
            email=fake.email()
        )
    return HttpResponse("50 records inserted successfully.")
def person_list(request):
    valid_sort_fields = ["name", "age", "created_at"]  # Ensure only valid fields can be sorted
    sort_by = request.GET.get('sort', 'name')  # Default sort field
    order = request.GET.get('order', 'asc')  # Default order

    if sort_by not in valid_sort_fields:
        sort_by = 'name'  # Fallback to default if invalid

    if order == "desc":
        sort_by = f"-{sort_by}"

    persons = Person.objects.all().order_by(sort_by)
    return render(request, 'person_list.html', {'persons': persons, 'sort_by': sort_by, 'order': order})
