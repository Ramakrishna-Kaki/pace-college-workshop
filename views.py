from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages
from django.http import HttpResponse


# Register View
def register(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone_number = request.POST.get("phone_number")

        # Check if email already exists
        if Users.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")

        # Save user data
        Users.objects.create(
            name=name,
            email=email,
            password=password,
            phone_number=phone_number
        )

        messages.success(request, "Registration Successful")
        return redirect("login")

    return render(request, "register.html")


# Login View
def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check email and password
        user = Users.objects.filter(
            email=email,
            password=password
        ).first()

        if user:
            messages.success(request, "Login Successful")
            return redirect("home")
        else:
            messages.error(request, "Invalid Email or Password")
            return redirect("login")

    return render(request, "login.html")



def home(request):
    return HttpResponse("Welcome Home")