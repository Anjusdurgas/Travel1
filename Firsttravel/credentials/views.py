from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        fname = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        print("here")
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                print("here1")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                print("here2")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=fname,last_name=last_name,password=password,email=email)
                print("here3")
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Passwords not matched")
            print("here4")
            return redirect('register')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')