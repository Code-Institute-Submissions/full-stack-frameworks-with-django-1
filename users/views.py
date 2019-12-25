from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import UserRegistrationForm, UserEmailUpdateForm


def register_view(request):
    """
        View for a user registration form
        on the front-end
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} has been created!')
            return redirect('user-login')
    else:
        form = UserRegistrationForm()
    meta = {
        'title': 'Register for Issue Tracker',
    }
    context = {
        'meta': meta,
        'form': form,
    }
    return render(request, 'users/register.html', context)


@login_required
def profile_view(request):
    """
        View for a specific user profile
        on the front-end
    """
    meta = {
        'title': 'User Profile',
    }
    context = {
        'meta': meta,
    }
    return render(request, 'users/profile.html', context)


@login_required
def change_email_view(request):
    """
        Edit a specific user email
        on the front-end
    """
    if request.method == 'POST':
        update_form = UserEmailUpdateForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('user-profile')
    else:
        update_form = UserEmailUpdateForm(instance=request.user)
    meta = {
        'title': 'Change Email Address',
    }
    context = {
        'meta': meta,
        'update_form': update_form,
    }
    return render(request, 'users/change-email.html', context)


@login_required
def change_password_view(request):
    """
        Edit a specific user password
        on the front-end
    """
    if request.method == 'POST':
        update_form = PasswordChangeForm(data=request.POST, user=request.user)
        if update_form.is_valid():
            update_form.save()
            update_session_auth_hash(request, update_form.user)
            messages.success(request, f'Your account has been updated.')
            return redirect('user-profile')
        else:
            messages.error(request, 'There has been an error')
            return redirect('user-change-password')
    else:
        update_form = PasswordChangeForm(user=request.user)
    meta = {
        'title': 'Change Password',
    }
    context = {
        'meta': meta,
        'update_form': update_form,
    }
    return render(request, 'users/change-password.html', context)
