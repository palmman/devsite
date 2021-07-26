from django.shortcuts import redirect, render
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.response import Response
from .serializers import ProjectsSerializer
from project.models import Project, Review

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProjects(request):
    projects = Project.objects.all()
    # if request.method == 'GET':
    serializer = ProjectsSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request, pk):
    projects = Project.objects.get(id=pk)
    # if request.method == 'GET':
    serializer = ProjectsSerializer(projects, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        owner = user,
        project = project,

    )

    review.value = data['value']
    review.save()
    project.getVoteCount

    serializers = ProjectsSerializer(project, many = False)
    return Response(serializers.data)