from django.shortcuts import render, redirect
from core.models import Subject, Home, Signin, Signup


def subject(request):
    if request.method == "POST":
        name = request.POST.get("subject_name")
        if name:
            Subject.objects.create(name=name)
        return redirect("subject")

    subjects = Subject.objects.all()
    return render(request, "subject.html", {"subjects": subjects})


def home(request):
    if request.method == "GET":
        return render(request, "home.html")

    homes = Home.objects.all()
    return render(request, "home.html", {"homes": homes})


def signin(request):
    if request.method == "POST":
        id = request.POST.get("id")
        password = request.POST.get("password")
        if id and password:
            Signin.objects.create(id=id, password=password)
        return redirect("signin")

    signins = Signin.objects.all()
    return render(request, "signin.html", {"signins": signins})


def signup(request):
    if request.method == "POST":
        id = request.POST.get("id")
        password = request.POST.get("password")
        username = request.POST.get("username")
        if id and password and username:
            Signup.objects.create(id=id, password=password, username=username)
        return redirect("signup")

    signups = Signup.objects.all()
    return render(request, "signup.html", {"signups": signups})
