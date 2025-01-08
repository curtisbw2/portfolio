from django.shortcuts import render, redirect
from .models import Project
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    projects = Project.objects.all()  # Fetch all projects
    return render(request, 'home.html', {'projects': projects})

def resume(request):
    return render(request, 'resume.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        send_mail(
            subject=f"Portfolio Contact from {name}",
            message=f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['curtisbw2@gmail.com'], 
            fail_silently=False
        )
        
        return redirect('contact-thank-you')

    return render(request, 'contact.html')

def contact_thanks_view(request):
    """Renders a simple 'thank you' page."""
    return render(request, 'contact_thanks.html')