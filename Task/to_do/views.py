from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import CreateTaskForm
from django.contrib import messages


def newtask(request):
    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The task is created  successfully!')
            return redirect('Home')
        else:
            messages.error(request, 'The task is not created  successfully!')
    return render(request, "to_do/new_task.html", {'form': form})


def taskupdate(request, pk):
    data = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, 'The task was updated  successfully!')
            return redirect('Home')
    else:
        form = CreateTaskForm(instance=data)
        context = {'form': form}
        return render(request, "to_do/task_update.html", context)


def taskview(request, pk):
    special_task = get_object_or_404(Task, pk=pk)
    return render(request, "to_do/task_view.html", {'task': special_task})

def home(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, "to_do/home.html", context)


def taskdelete(request, pk):
    task_to_delete = get_object_or_404(Task, pk=pk)
    task_to_delete.delete()
    messages.success(request, 'The task was deleted!')
    return redirect('Home')