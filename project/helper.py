from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginationProject(request, projects, results):

    page = request.GET.get('page')
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 3)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, projects

def projectSearch(request):

    search = ''

    if request.GET.get('value'):
        search = request.GET.get('value')

    tags = Tag.objects.filter(name__icontains=search)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search) |
        Q(description__icontains=search) |
        Q(owner__name__icontains=search) |
        Q(tags__in=tags)
    ).order_by('-created')

    return projects, search