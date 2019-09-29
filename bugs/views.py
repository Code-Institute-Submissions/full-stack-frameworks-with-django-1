from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Bug, Comment
from .forms import BugForm, CommentForm


def get_bugs_view(request):
    """
        View that returns a list of
        Bugs that are published.
    """
    bugs = {
        'all': Bug.objects.filter(status='IP'),
        # 'users': Bug.objects.filter(author_id=request.user, status='IP'),
        'critical': Bug.objects.filter(priority='CRITICAL', status='IP'),
        'high': Bug.objects.filter(priority='HIGH', status='IP'),
        'medium': Bug.objects.filter(priority='MEDIUM', status='IP'),
        'low': Bug.objects.filter(priority='LOW', status='IP'),
    }
    context = {
        'bugs': bugs,
    }
    return render(request, 'bugs/get-bugs.html', context)


@login_required
def get_user_bugs_view(request):
    """
        View that returns a list of
        Bugs that a user has published
    """
    bugs = {
        'users': Bug.objects.filter(author_id=request.user, status='IP'),
    }
    context = {
        'bugs': bugs,
    }
    return render(request, 'bugs/get-user-bugs.html', context)


def bug_detail_view(request, pk):
    """
        View for a single bug object, using
        the pk (primary key) aka ID.

        404 if not found.
    """
    context = {
        'bug': get_object_or_404(Bug, pk=pk),
        'comments': Comment.objects.filter(bug=pk),
    }
    return render(request, 'bugs/bug-detail.html', context)


@login_required
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


@login_required
def create_or_edit_comment_view(request, bug_pk, pk=None):
    """
        View that allows either create or
        update f unctionality depending on
        if the Comment ID is null or not
    """
    bug = get_object_or_404(Bug, pk=bug_pk)
    comment = get_object_or_404(Comment, pk=pk) if pk else None
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.bug = bug
            form.save()
            return redirect('bug-detail', bug_pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'bugs/comment-form.html', {'form': form})
