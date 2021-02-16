from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('newtask/', views.newtask, name='NewTask'),
    path('taskupdate/', views.taskupdate, name='TaskUpdate'),
    path('taskview/', views.taskview, name='TaskView'),
]