from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()  # Fetch all projects
    return render(request, 'home.html', {'projects': projects})

def resume(request):
    return render(request, 'resume.html')
