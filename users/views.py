from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


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
            messages.success(request, f'Your account has been created {username}!')
            return redirect('main-homepage')
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
