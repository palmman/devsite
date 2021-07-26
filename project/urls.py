from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project-object/<str:pk>', views.project, name='project'),
    path('create-object', views.createProject, name='createProject'),
    path('update-object/<str:pk>', views.updateProject, name='updateProject'),
    path('delete-object/<str:pk>', views.deleteProject, name='deleteProject'),
]