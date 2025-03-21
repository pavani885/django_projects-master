from django.shortcuts import render
def student_list(request):
    students = [
        {'name': 'Rama', 'marks': 75},
        {'name': 'Lakshman', 'marks': 20},
        {'name': 'seetha', 'marks': 55},
        {'name': 'Ravana', 'marks': 40},
    ]
    passing_marks = 30  
    return render(request, 'recordapp/student_list.html', {'students': students, 'passing_marks': passing_marks})

