from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('newtask/', views.newtask, name='NewTask'),
    path('taskupdate/', views.taskupdate, name='TaskUpdate'),
    path('taskview/<int:pk>', views.taskview, name='TaskView'),
    path('', views.home, name='Home'),
    path('taskdelete/<int:pk>', views.taskdelete, name='TaskDelete'),
]