from django.contrib import auth
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.
def loginview(request):
    return render(request,'course1/login.html')
    # return render(request,'members/Cartpage.html')
def signupview(request):
    return render(request,'course1/Signup.html')

    # return render(request,'members/Cartpage.html')
def loginsubmit(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    print(username)
    print(password)
    user=authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        messages.add_message(request,messages.SUCCESS,"Login suceess")
        return redirect("/shop/")
    else:
        messages.add_message(request,messages.ERROR,"email or password is not valid")
        return redirect("/members/login")
    



def signsubmit(request):
    
    if(request.method=="POST"):
        username=request.POST.get("username")
        f_name=request.POST.get("first_name")
        l_name=request.POST.get("last_name")
        password=request.POST.get("password")
        passwordagain=request.POST.get("passwordagain")
        # validation access
        if(not {len(password)>7 and not password.isalnum()}):
            messages.add_message(request,messages.ERROR,"password nust be longer than 7")
            return redirect("/members/signup")
        else:
            NewUser=User.objects.create_user(username,username,password)
            NewUser.first_name=f_name
            NewUser.last_name=l_name
            NewUser.save()
            print(l_name)
            return redirect("/members/login")
    
    
    else:
        messages.add_message(request,messages.ERROR,"Please sign in ")
        return HttpResponse("signup failed")

def logoutkr(request):
    auth.logout(request)
    messages.add_message(request,messages.ERROR,"Logout")
    return redirect("/")
