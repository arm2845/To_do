from django.shortcuts import render, redirect


def newtask(request):
    return render(request, "todo/new_task.html")


def taskupdate(request):
    return render(request, "todo/task_update.html")


def taskview(request):
    return render(request, "todo/task_view.html")
