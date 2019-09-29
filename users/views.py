from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm


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
    return render(request, 'users/profile.html')


@login_required
def edit_profile_view(request):
    """
        Edit a specific user profile
        on the front-end
    """
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('user-profile')
    else:
        update_form = UserUpdateForm(instance=request.user)
    context = {
        'update_form': update_form,
    }
    return render(request, 'users/edit-profile.html', context)
