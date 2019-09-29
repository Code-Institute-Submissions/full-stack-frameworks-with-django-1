from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Bug
from .forms import BugForm, CommentForm


def get_bugs_view(request):
    """
        View that returns a list of
        Bugs that are published.
    """
    bugs = {
        'all': Bug.objects.filter(status='IP'),
        'critical': Bug.objects.filter(priority='CRITICAL', status='IP'),
        'high': Bug.objects.filter(priority='HIGH', status='IP'),
        'medium': Bug.objects.filter(priority='MEDIUM', status='IP'),
        'low': Bug.objects.filter(priority='LOW', status='IP'),
    }
    context = {
        'bugs': bugs,
    }
    return render(request, 'bugs/get-bugs.html', context)


def bug_detail_view(request, pk):
    """
        View for a single bug object, using
        the pk (primary key) aka ID.

        404 if not found.
    """
    context = {
        'bug': get_object_or_404(Bug, pk=pk),
    }
    return render(request, 'bugs/bug-detail.html', context)


def create_or_edit_bug_view(request, pk=None):
    """
        View that allows either create or
        update functionality depending on
        if the Bug ID is null or not 
    """
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.method == 'POST':
        form = BugForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            form.instance.author = request.user
            bug = form.save()
            return redirect('bug-detail', bug.pk)
    else:
        form = BugForm(instance=bug)
    return render(request, 'bugs/bug-form.html', {'form': form})
