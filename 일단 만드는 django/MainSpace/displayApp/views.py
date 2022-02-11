from django.shortcuts import render

def first(request):
    return render(request, 'first_display.html')

def second(request):
    return render(request, 'second_display.html')