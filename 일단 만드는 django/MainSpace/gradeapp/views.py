from django.shortcuts import render

def grade(request):
    return render(request, 'grade.html')

def first_grade(request):
    return render(request, 'first_grade.html')