from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    projects = Project.objects.filter(is_published=True).order_by('-created_on')
    
    
    technology = request.GET.get('technology')
    if technology:
        projects = projects.filter(technology=technology)
    
    context = {
        'projects': projects,
        'technology_filter': technology
    }
    return render(request, 'projects/project_list.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, is_published=True)
    context = {
        'project': project
    }
    return render(request, 'projects/project_detail.html', context)