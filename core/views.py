from django.shortcuts import render, redirect
from core.models import Subject

def subject(request):
    if request.method == 'POST':
        name = request.POST.get('subject_name')
        if name:
            Subject.objects.create(name=name)
        return redirect('subject')
    
    subjects = Subject.objects.all()
    return render(request, 'subject.html', {'subjects': subjects})
