from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Bug, Comment, Upvote, SavedBug
from .forms import BugForm, CommentForm, UpvoteForm, SavedBugForm


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


@login_required
def user_save_bug(request, pk):
    """
        Allow the user to save a
        bug, if they wish to keep
        an eye on it
    """
    bug = Bug.objects.get(pk=pk)
    sb_form = SavedBugForm(request.POST or None)
    if request.method == 'POST':
        if sb_form.is_valid():
            user = request.user
            try:
                saved_bug = SavedBug.objects.get(user=user, bug=bug)
            except SavedBug.DoesNotExist:
                saved_bug = None
            if saved_bug is None:
                saved_bug = SavedBug(user=user, bug=bug)
                saved_bug.save()
                messages.success(request, 'success')
            else:
                messages.error(request, 'error')
    return redirect('bug-detail', bug.pk)


@login_required
def get_user_saved_bugs_view(request):
    """
        View that returns a list of
        Bugs that a user has saved
    """
    bugs = {
        'saved': SavedBug.objects.filter(user_id=request.user),
    }
    context = {
        'bugs': bugs,
    }
    return render(request, 'bugs/get-user-saved-bugs.html', context)


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
def create_bug_view(request, pk=None):
    """
        View that allows either create or
        update functionality depending on
        if the Bug ID is null or not 
    """
    # bug = get_object_or_404(Bug, pk=pk) if pk else None
    # if request.method == 'POST':
    #     form = BugForm(request.POST, request.FILES, instance=bug)
    #     if form.is_valid():
    #         form.instance.author = request.user
    #         bug = form.save()
    #         return redirect('bug-detail', bug.pk)
    # else:
    #     form = BugForm(instance=bug)
    # return render(request, 'bugs/bug-form.html', {'form': form})

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
def edit_bug_view(request, pk=None):
    """
        View that allows either create or
        update functionality depending on
        if the Bug ID is null or not 
    """
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.user == bug.author:
        if request.method == 'POST':
            form = BugForm(request.POST, request.FILES, instance=bug)
            if form.is_valid():
                bug = form.save()
                messages.success(request, 'success')
        else:
            form = BugForm(instance=bug)
        return render(request, 'bugs/bug-form.html', {'form': form})
    else:
        messages.error(request, 'error')
        return redirect('bug-detail', bug.pk)


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


@login_required
def upvote_bug_view(request, pk):
    """
        Allow users to upvote a bug
    """
    bug = Bug.objects.get(pk=pk)
    uv_form = UpvoteForm(request.POST or None)
    if request.method == 'POST':
        if uv_form.is_valid():
            user = request.user
            try:
                has_voted = Upvote.objects.get(user=user, bug=bug)
            except Upvote.DoesNotExist:
                has_voted = None
            if has_voted is None:
                has_voted = Upvote(user=user, bug=bug)
                has_voted.save()
                bug.upvotes += 1
                bug.save()
                messages.success(request, 'success')
            else:
                messages.error(request, 'error')
    return redirect('bug-detail', bug.pk)
