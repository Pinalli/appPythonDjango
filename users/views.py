from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def register(request):  
    if request.method == 'GET':       
         return render(request, 'register.html')
    elif request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')        
        password = request.POST.get('password')        
        email = request.POST.get('email')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
              messages.add_message(request, constants.ERROR, 'Passwords not equals')
              return redirect('/users/register')
        
        if len(password) < 6:
              messages.add_message(request, constants.ERROR, 'Your password must be at least 6 characters long')
              return redirect('/users/register')
      
        try:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name, 
                username=username, 
                password=password, 
                email=email
             )
            messages.add_message(request, constants.SUCCESS, 'Registered successfully')
        except Exception as e:
            messages.add_message(request, constants.ERROR, 'Error registering user, contact the administrator')           
            return redirect('/users/register')
        return  redirect('/users/register')

def log_in(request):
    if request.method == 'GET':       
         return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')        
        password = request.POST.get('password')  

        user = authenticate(username=username, password=password)
        if user:
           login(request, user)
           return redirect('/')
        else:
            messages.add_message(request, constants.ERROR, 'Incorrect username or password')
            return redirect('/users/login')