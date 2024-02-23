from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate
from django.contrib import auth

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None: 
            auth.login(request,user)
            return redirect('/index')
        else:
            messages.info(request,'Credentials Invalid !!')
            return redirect('/')
    return render(request,'login.html')



def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email alrady taken')
                return redirect('/signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username alrady taken')
                return redirect('/signup')
            else:
                user =User.objects.create_user(username=username,email=email,password=password)
                user.save()
                
                return redirect('/')
                
        else:
            messages.info(request,'Password is Not Matching')
            return redirect('/signup')
        
    else:
        return render(request,'signup.html')