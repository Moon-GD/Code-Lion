from django.shortcuts import render, redirect
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        id = request.POST['ID']
        pw = request.POST['PASSWORD']
        user = auth.authenticate(request, username=id, password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('home')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'index.html')