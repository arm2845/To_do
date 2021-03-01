from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import CreateTaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required()
def all_tasks(request):

    if request.user.is_superuser:
        tasks = Task.objects.all()
        context = {'tasks': tasks}
        return render(request, "to_do/home.html", context)
    else:
        return JsonResponse('bad request', safe=False)


@login_required()
def newtask(request):
    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = get_object_or_404(User, pk=request.user.id)
            task.save()
            messages.success(request, 'The task is created  successfully!')
            return redirect('Home')
        else:
            messages.error(request, 'The task is not created  successfully!')
    return render(request, "to_do/new_task.html", {'form': form})


@login_required()
def taskupdate(request, pk):

    if request.user.is_superuser:
        data = get_object_or_404(Task, pk=pk)
    else:
        data = get_object_or_404(Task, pk=pk, user=request.user.id)

    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, 'The task was updated successfully!')
            return redirect('TaskView', pk=pk)
    else:
        form = CreateTaskForm(instance=data)
        return render(request, "to_do/task_update.html", {'form': form})


# @login_required()
# def taskview(request, pk):
#     special_task = get_object_or_404(Task, pk=pk, user=request.user.id)
#     return render(request, "to_do/task_view.html", {'task': special_task})


# @login_required()
# def home(request):
#     tasks = Task.objects.all().filter(user=request.user.id)
#     context = {'tasks': tasks}
#     return render(request, "to_do/home.html", context)


class HomeView(LoginRequiredMixin, ListView):
    model = Task
    def get_queryset(self):
        return self.model.objects.all().filter(user=self.request.user)


class TaskView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "to_do/task_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = "Hello world"
        return context


@login_required()
def taskdelete(request, pk):
    task_to_delete = get_object_or_404(Task, pk=pk, user=request.user.id)
    task_to_delete.delete()
    messages.success(request, 'The task was deleted!')
    return redirect('Home')