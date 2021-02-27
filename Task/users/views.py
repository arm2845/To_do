from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile


@login_required
def profile_page(request):
    profile = Profile.objects.get(id=request.user.id)
    return render(request, "users/profile.html", {'profile': profile})


def create(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.data.get('username')
            password = form.data.get('password1')
            first_name = form.data.get('first_name')
            last_name = form.data.get('last_name')
            user = authenticate(request, username=username, password=password, first_name=first_name,last_name=last_name)
            if user is not None:
                login(request, user)
            return redirect('ProfilePage')
    return render(request, 'users/create.html', {'form': form})
