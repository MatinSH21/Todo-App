from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserUpdateForm


class UserLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('task-list')


class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have created an account successfully. You can Login now!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', context={'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated your profile!')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', context={'form': form})
