from django.urls import path
from . import views
from .views import contact_view, contact_thanks_view

urlpatterns = [
    path('', views.home, name='home'),
    path('resume/', views.resume, name='resume'),
    path('contact/', contact_view, name='contact'),
    path('contact/thank-you/', contact_thanks_view, name='contact-thank-you'),
]