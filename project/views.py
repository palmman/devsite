from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.contrib import messages
from .models import Project, Tag
from .form import ProjectForm, ReviewForm
from .helper import projectSearch, paginationProject 

# Create your views here.

def projects(request):

    projects, search = projectSearch(request)

    custom_range, projects = paginationProject(request, projects, 3)
    

    context = {
        'projects':projects,
        'search':search,
        'custom_range':custom_range,
    }
    return render(request, 'projects/project.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)

    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        review.save()

        project.getVoteCount

        messages.success(request, 'Your review was successfully.')
        return redirect('project', pk=project.id)
    



    context = {
        'project':project,
        'form':form,
    }
    return render(request, 'projects/single_project.html',context)

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    
    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid:
            project = form.save()
            project.owner = profile
            project.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
    context = {
        'form':form,
    }
    return render(request, 'projects/create_project.html',context)

@login_required(login_url='login')
def updateProject(request, pk):

    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()        
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid:
            form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
    context = {
        'form':form,
    }
    return render(request, 'projects/create_project.html',context)
    

@login_required(login_url='login')
def deleteProject(request, pk):

    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('account')

    context = {
        'object':project,
    }
    return render(request, 'delete_template.html',context)