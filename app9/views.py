from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"app9/home.html")

def profile(request):
    name="rocky"
    return render(request,"app9/profile.html",{'name':name})

def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        phonenumber=request.POST.get("phone number")
        gender=request.POST.get("gender")
        DOB=request.POST.get("DOB")
        send_mail("thanks for registration","hello {} {}\n thanks for tregistering ".format(first_name,last_name),
        "roopendrark@gmail.com",[email,],fail_silently=False)
        return redirect("home")
    return render(request,"app9/registration.html")