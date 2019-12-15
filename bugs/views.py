from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Bug, Comment, Upvote, SavedBug
from .forms import BugForm, CommentForm, UpvoteForm, SavedBugForm


def get_bugs_view(request):
    """
        View that returns a list of
        Bugs that are published.
    """
    per_page = 4
    a_bugs = (Paginator(Bug.objects
              .filter(status='IP')
              .order_by('-upvotes'), per_page))
    page = request.GET.get('page')
    all_bugs_paged = a_bugs.get_page(page)
    bugs = all_bugs_paged
    context = {
        'bugs': bugs,
    }
    return render(request, 'bugs/get-bugs.html', context)


def get_bugs_priority_view(request, priority):
    """
        View that returns a list of
        Bugs that are published
        based on their priority.
    """
    per_page = 4
    c_bugs = (Paginator(Bug.objects
              .filter(priority='CRITICAL', status='IP')
              .order_by('-upvotes'), per_page))
    h_bugs = (Paginator(Bug.objects
              .filter(priority='HIGH', status='IP')
              .order_by('-upvotes'), per_page))
    m_bugs = (Paginator(Bug.objects
              .filter(priority='MEDIUM', status='IP')
              .order_by('-upvotes'), per_page))
    l_bugs = (Paginator(Bug.objects
              .filter(priority='LOW', status='IP')
              .order_by('-upvotes'), per_page))
    page = request.GET.get('page')
    critical_bugs_paged = c_bugs.get_page(page)
    high_bugs_paged = h_bugs.get_page(page)
    medium_bugs_paged = m_bugs.get_page(page)
    low_bugs_paged = l_bugs.get_page(page)
    priority = priority
    if priority == 'critical':
        bugs = critical_bugs_paged
    elif priority == 'high':
        bugs = high_bugs_paged
    elif priority == 'medium':
        bugs = medium_bugs_paged
    elif priority == 'low':
        bugs = low_bugs_paged
    else:
        messages.error(request, 'Error! That is not a recognised priority.')
        return redirect('get-bugs')
    context = {
        'bugs': bugs,
        'priority': priority,
    }
    return render(request, 'bugs/get-bugs-priority.html', context)


@login_required
def get_user_bugs_view(request):
    """
        View that returns a list of
        Bugs that a user has published
    """
    per_page = 4
    u_bugs = (Paginator(Bug.objects
              .filter(author=request.user, status='IP')
              .order_by('-upvotes'), per_page))
    page = request.GET.get('page')
    user_bugs_paged = u_bugs.get_page(page)
    bugs = user_bugs_paged
    context = {
        'bugs': bugs,
    }
    return render(request, 'bugs/get-user-bugs.html', context)


@login_required
def get_user_saved_bugs_view(request):
    """
        View that returns a list of
        Bugs that a user has saved
    """
    per_page = 4
    s_bugs = (Paginator(SavedBug.objects
              .filter(user=request.user)
              .order_by('-date_created'), per_page))
    page = request.GET.get('page')
    saved_bugs_paged = s_bugs.get_page(page)
    bugs = saved_bugs_paged
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
    bug = get_object_or_404(Bug, pk=pk)
    comments = Comment.objects.filter(bug=pk)
    if request.user.is_authenticated:
        try:
            is_saved = SavedBug.objects.get(user=request.user, bug=bug)
        except SavedBug.DoesNotExist:
            is_saved = None
    else:
        is_saved = None
    context = {
        'bug': bug,
        'comments': comments,
        'is_saved': is_saved,
    }
    return render(request, 'bugs/bug-detail.html', context)


@login_required
def create_bug_view(request, pk=None):
    """
        View that allows the user
        to create a new bug
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
def edit_bug_view(request, pk=None):
    """
        View that allows the user
        to edit an existing bug
        if it belongs to them
    """
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.user == bug.author:
        if request.method == 'POST':
            form = BugForm(request.POST, request.FILES, instance=bug)
            if form.is_valid():
                bug_status = form.instance.status
                if bug_status == 'IP':
                    bug.date_completed = None
                elif bug_status == 'C' and bug.date_completed is None:
                    bug.date_completed = datetime.now()
                bug = form.save()
                messages.success(request,
                                 'Success! Edit has been successfully saved.')
                return redirect('bug-detail', bug.pk)
        else:
            form = BugForm(instance=bug)
        return render(request, 'bugs/bug-form.html', {'form': form})
    else:
        messages.error(request,
                       'Error! You are not permitted to edit this bug.')
        return redirect('bug-detail', bug.pk)


@login_required
def delete_bug_view(request, pk=None):
    """
        View that allows the user
        to delete an existing bug
        if it belongs to them
    """
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.user == bug.author and request.method == 'POST':
        bug.delete()
        messages.success(request,
                         'Success! Bug has been successfully deleted.')
        return redirect('get-bugs')
    else:
        messages.error(request,
                       'Error! You are not permitted to delete this bug.')
        return redirect('bug-detail', bug.pk)


@login_required
def create_or_edit_comment_view(request, bug_pk, pk=None):
    """
        View that allows either create or
        update functionality depending on
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
                messages.success(request,
                                 'Success! You have upvoted this bug.')
            else:
                messages.error(request,
                               'Error! You have already voted once.')
    return redirect('bug-detail', bug.pk)


@login_required
def user_save_bug_view(request, pk):
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
                messages.success(request,
                                 'Success! You have added this '
                                 'bug to your saved bugs.')
            else:
                messages.error(request,
                               'Error! You have already saved this bug.')
    return redirect('bug-detail', bug.pk)


@login_required
def delete_saved_bug_view(request, pk):
    """
        View that allows the user
        to delete an existing saved bug
        if it belongs to them
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
            if saved_bug is not None:
                saved_bug.delete()
                messages.success(request,
                                 'Success! You have removed this '
                                 'bug from your saved bugs.')
                return redirect('bug-detail', bug.pk)
            else:
                messages.error(request,
                               'Error! You have already removed this bug.')
    return redirect('bug-detail', bug.pk)
