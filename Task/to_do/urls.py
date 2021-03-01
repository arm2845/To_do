from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view(template_name="to_do/home.html"), name='Home'),
    path('newtask/', views.newtask, name='NewTask'),
    path('taskupdate/<str:pk>', views.taskupdate, name='TaskUpdate'),
    path('taskview/<int:pk>', views.TaskView.as_view(), name='TaskView'),
    path('taskdelete/<int:pk>', views.taskdelete, name='TaskDelete'),
    path('all_tasks', views.all_tasks, name='AllTasks'),
]