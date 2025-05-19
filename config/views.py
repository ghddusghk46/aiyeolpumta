from django.shortcuts import render

def subject(request):
    return render(request, "subject.html")
