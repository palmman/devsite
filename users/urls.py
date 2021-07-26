from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('edit_account/', views.edit_account, name='edit_account'),
    path('create_skill/', views.create_skill, name='create_skill'),
    path('edit_skill/<str:pk>', views.edit_skill, name='edit_skill'),
    path('delete_skill/<str:pk>', views.delete_skill, name='delete_skill'),


    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:pk>', views.inboxMessage, name='message'),
    path('create-message/<str:pk>', views.createMessage, name='create-message'),

    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.user_profile, name='user_profile'),
]
