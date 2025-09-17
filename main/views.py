from django.shortcuts import render
from projects.models import Project

def home_view(request):
    featured_projects = Project.objects.filter(is_published=True).order_by('-created_on')[:3]
    
    context = {
        'featured_projects': featured_projects
    }
    return render(request, 'main/home.html', context)

def about_view(request):
    context = {
        'skills': [
            {'name': 'Python', 'level': 80},
            {'name': 'Django', 'level': 85},
            {'name': 'PostgreSQL', 'level': 80},
            {'name': 'HTML/CSS', 'level': 60},
            {'name': 'JavaScript', 'level': 55},
            {'name': 'Docker', 'level': 90},
        ],
    }
    return render(request, 'main/about.html', context)

def contact_view(request):
    return render(request, 'main/contact.html')