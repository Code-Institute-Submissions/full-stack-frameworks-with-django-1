from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Ticket, Comment, Upvote, SavedTicket
from .forms import BugForm, FeatureForm, CommentForm, UpvoteForm, SavedTicketForm, FilterForm


def get_tickets_view(request):
    """
        View that returns a list of
        tickets (both bugs and features)
        that are published.
    """
    per_page = 4
    a_tickets = (Paginator(Ticket.objects
                 # .exclude(status='C')
                 .order_by('-upvotes'), per_page))
    page = request.GET.get('page')
    all_tickets_paged = a_tickets.get_page(page)
    tickets = all_tickets_paged
    meta = {
        'title': 'All Tickets',
    }
    context = {
        'meta': meta,
        'tickets': tickets,
    }
    return render(request, 'tickets/get-tickets.html', context)


def get_tickets_tag_view(request, tag):
    """
        View that returns a list of
        tickets depending on tag e.g.
        bugs or features (that are published).
    """
    mandatory_tags = ['bug', 'feature']
    if Ticket.objects.filter(tag=tag).exists() or \
    tag in mandatory_tags:
        per_page = 4
        filtered_tickets = (Paginator(Ticket.objects
                            .filter(tag=tag)
                            # .exclude(status='C')
                            .order_by('-upvotes'), per_page))
        page = request.GET.get('page')
        tickets = filtered_tickets.get_page(page)
        meta = {
            'title': 'All ' + tag.capitalize() + 's',
        }
        context = {
            'meta': meta,
            'tag': tag,
            'tickets': tickets,
        }
        return render(request, 'tickets/get-tickets.html', context)
    else:
        raise Http404('This type of ticket does not exist.')


def get_bugs_priority_view(request, priority):
    """
        View that returns a list of
        Bugs that are published based
        on their priority.
    """
    mandatory_priorities = ['critical', 'high', 'medium', 'low']
    if Ticket.objects.filter(priority=priority).exists() or \
    priority in mandatory_priorities:
        per_page = 4
        filtered_tickets = (Paginator(Ticket.objects
                            .filter(tag='bug', priority=priority)
                            .exclude(status='C')
                            .order_by('-upvotes'), per_page))
        page = request.GET.get('page')
        tickets = filtered_tickets.get_page(page)
        meta = {
            'title': priority.capitalize() + ' Priority',
        }
        context = {
            'meta': meta,
            'priority': priority,
            'tickets': tickets,
        }
        return render(request, 'tickets/get-bugs.html', context)
    else:
        raise Http404('This level of priority does not exist.')


@login_required
def get_user_tickets_view(request, tag):
    """
        View that returns a list of
        Tickets published by a specific
        user.

        Separated by Bugs/Features.
    """
    mandatory_tags = ['bug', 'feature']
    if Ticket.objects.filter(tag=tag).exists() or \
    tag in mandatory_tags:
        per_page = 4
        filtered_tickets = (Paginator(Ticket.objects
                            .filter(author=request.user, tag=tag)
                            .order_by('-date_created'), per_page))
        page = request.GET.get('page')
        tickets = filtered_tickets.get_page(page)
        meta = {
            'title': 'My Submitted ' + tag.capitalize() + 's',
        }
        context = {
            'meta': meta,
            'tag': tag,
            'tickets': tickets,
        }
        return render(request, 'tickets/get-user-tickets.html', context)
    else:
        raise Http404('This type of ticket does not exist.')


@login_required
def get_user_saved_tickets_view(request, tag):
    """
        View that returns a list of
        Tickets saved by a specific
        user.

        Separated by Bugs/Features.
    """
    mandatory_tags = ['bug', 'feature']
    if SavedTicket.objects.filter(ticket__tag=tag).exists() or \
    tag in mandatory_tags:
        per_page = 4
        filtered_tickets = (Paginator(SavedTicket.objects
                            .filter(user=request.user, ticket__tag=tag)
                            .order_by('-date_created'), per_page))
        page = request.GET.get('page')
        tickets = filtered_tickets.get_page(page)
        meta = {
            'title': 'My Saved ' + tag.capitalize() + 's',
        }
        context = {
            'meta': meta,
            'tag': tag,
            'tickets': tickets,
        }
        return render(request, 'tickets/get-user-saved-tickets.html', context)
    else:
        raise Http404('This type of ticket does not exist.')


def get_ticket_detail_view(request, pk):
    """
        View that returns a single ticket
        using the pk (primary key) aka ID.
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    comments = Comment.objects.filter(ticket=pk)
    if request.user.is_authenticated:
        try:
            is_saved = SavedTicket.objects.get(user=request.user, ticket=ticket)
        except SavedTicket.DoesNotExist:
            is_saved = None
    else:
        is_saved = None
    meta = {
        'title': ticket.title,
    }
    context = {
        'meta': meta,
        'ticket': ticket,
        'comments': comments,
        'is_saved': is_saved,
    }
    return render(request, 'tickets/ticket-detail.html', context)


@login_required
def add_new_ticket_view(request, tag, pk=None):
    """
        View that allows the user
        to create a new ticket.

        Different forms are shown
        for bugs and features.
    """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == 'POST':
        if tag == 'bug':
            form = BugForm(request.POST, request.FILES, instance=ticket)
            if form.is_valid():
                form.instance.author = request.user
                form.instance.upvote_price = None
                ticket = form.save()
                messages.success(request, 'Success! Bug created.')
                return redirect('get-ticket-detail', ticket.pk)
        elif tag == 'feature':
            form = FeatureForm(request.POST, instance=ticket)
            if form.is_valid():
                form.instance.author = request.user
                form.instance.tag = 'FEATURE'
                form.instance.priority = None
                form.instance.status = 'FR'
                ticket = form.save()
                messages.success(request, 'Success! Feature created.')
                return redirect('get-ticket-detail', ticket.pk)
        else:
            raise Http404('This type of ticket does not exist.')
    else:
        if tag == 'bug':
            form = BugForm(instance=ticket)
        elif tag == 'feature':
            form = FeatureForm(instance=ticket)
        else:
            raise Http404('This type of ticket does not exist.')
    meta = {
        'title': 'Add New ' + tag.capitalize(),
    }
    context = {
        'meta': meta,
        'tag': tag,
        'form': form,
    }
    return render(request, 'tickets/ticket-form.html', context)


@login_required
def edit_ticket_view(request, pk=None):
    """
        View that allows the user
        to edit an existing ticket
        if it belongs to them.

        Different forms are shown
        for bugs and features.
    """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.user == ticket.author or request.user.is_staff:
        if request.method == 'POST':
            if ticket.tag == 'BUG':
                form = BugForm(request.POST, request.FILES, instance=ticket)
            elif ticket.tag == 'FEATURE':
                form = FeatureForm(request.POST, instance=ticket)
            else:
                raise Http404('This type of ticket does not exist.')
            if form.is_valid():
                ticket_status = form.instance.status
                if ticket_status == 'C' and ticket.date_completed is None:
                    ticket.date_completed = datetime.now()
                else:
                    ticket.date_completed = None
                ticket = form.save()
                messages.success(request, 'Success! Edit has been successfully saved.')
                return redirect('get-ticket-detail', ticket.pk)
        else:
            if ticket.tag == 'BUG':
                form = BugForm(instance=ticket)
            elif ticket.tag == 'FEATURE':
                form = FeatureForm(instance=ticket)
            else:
                raise Http404(ticket.tag)
            meta = {
                'title': 'Edit ' + ticket.tag.capitalize(),
            }
            context = {
                'meta': meta,
                'form': form,
            }
            return render(request, 'tickets/ticket-form.html', context) 
    else:
        messages.error(request,
                       'Error! You are not permitted to edit this bug.')
        return redirect('get-ticket-detail', ticket.pk)


@login_required
def delete_ticket_view(request, pk=None):
    """
        View that allows the user
        to delete an existing ticket
        if it belongs to them.
    """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.user == ticket.author and request.method == 'POST':
        ticket.delete()
        messages.success(request, 'Success! Ticket has been successfully deleted.')
        return redirect('get-tickets-tag', ticket.tag.lower())
    else:
        messages.error(request, 'Error! You are not permitted to delete this ticket.')
        return redirect('get-ticket-detail', ticket.pk)


@login_required
def add_new_comment_view(request, ticket_pk, pk=None):
    """
        View that allows the user
        to create a comment on
        a ticket.
    """
    ticket = get_object_or_404(Ticket, pk=ticket_pk)
    comment = get_object_or_404(Comment, pk=pk) if pk else None
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.ticket = ticket
            form.save()
            messages.success(request, 'Success! You have posted a comment.')
            return redirect('get-ticket-detail', ticket.pk)
    else:
        form = CommentForm(instance=comment)
    meta = {
        'title': 'Leave a Comment',
    }
    context = {
        'meta': meta,
        'form': form,
    }
    return render(request, 'tickets/comment-form.html', context)


def edit_comment_view(request):
    """
        View that allows the user
        to edit their comment on
        a ticket.
    """
    pass


def delete_comment_view(request):
    """
        View that allows the user
        to delete their comment on
        a ticket.
    """
    pass


@login_required
def upvote_bug_view(request, pk):
    """
        View that allows the user
        to upvote a ticket with
        the 'bug' tag.
    """
    ticket = Ticket.objects.get(pk=pk)
    form = UpvoteForm(request.POST or None)
    if request.method == 'POST' and ticket.tag == 'BUG':
        if form.is_valid():
            user = request.user
            try:
                has_voted = Upvote.objects.get(user=user, ticket=ticket)
            except Upvote.DoesNotExist:
                has_voted = None
            if has_voted is None:
                has_voted = Upvote(user=user, ticket=ticket)
                has_voted.save()
                ticket.upvotes += 1
                ticket.save()
                messages.success(request, 'Success! You have upvoted this bug.')
            else:
                messages.error(request, 'Error! You have already voted.')
    else:
        messages.error(request, 'Error! This ticket is not a bug.')
    return redirect('get-ticket-detail', ticket.id)


@login_required
def upvote_feature_view(request, pk):
    """
        View that allows the user
        to upvote a ticket with
        the 'feature' tag.
    """
    pass


@login_required
def user_save_ticket_view(request, pk):
    """
        View that allows the user
        to save a ticket.
    """
    ticket = Ticket.objects.get(pk=pk)
    form = SavedTicketForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = request.user
            try:
                saved_ticket = SavedTicket.objects.get(user=user, ticket=ticket)
            except SavedTicket.DoesNotExist:
                saved_ticket = None
            if saved_ticket is None:
                saved_ticket = SavedTicket(user=user, ticket=ticket)
                saved_ticket.save()
                messages.success(request, 'Success! You have saved this ticket.')
            else:
                messages.error(request, 'Error! You have already saved this ticket.')
    return redirect('get-ticket-detail', ticket.pk)


@login_required
def user_delete_saved_ticket_view(request, pk):
    """
        View that allows the user
        to remove a ticket that
        they have saved.
    """
    ticket = Ticket.objects.get(pk=pk)
    form = SavedTicketForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = request.user
            try:
                saved_ticket = SavedTicket.objects.get(user=user, ticket=ticket)
            except SavedTicket.DoesNotExist:
                saved_ticket = None
            if saved_ticket is not None:
                saved_ticket.delete()
                messages.success(request, 'Success! You have removed this ticket.')
                return redirect('get-ticket-detail', ticket.pk)
            else:
                messages.error(request, 'Error! You have already removed this ticket.')
    return redirect('get-ticket-detail', ticket.pk)


def is_valid_param(param):
    """
        Helper function to check
        if param is valid for the
        filter_tickets_view.
    """
    return param is not '' and param is not None


def filter_tickets_view(request):
    """
        View that allows the user
        to filter tickets however
        they choose.
    """
    form = FilterForm(request.GET)
    queryset = Ticket.objects.all()
    title_or_author_query = request.GET.get('title_or_author')
    tag_query = request.GET.get('tag')
    priority_query = request.GET.get('priority')
    status_query = request.GET.get('status')

    if is_valid_param(title_or_author_query):
        queryset = queryset.filter(Q(title__icontains=title_or_author_query) | Q(author__username__icontains=title_or_author_query)).distinct()

    if is_valid_param(tag_query):
        queryset = queryset.filter(tag=tag_query)

    if is_valid_param(priority_query):
        queryset = queryset.filter(priority=priority_query)

    if is_valid_param(status_query):
        queryset = queryset.filter(status=status_query)

    meta = {
        'title': 'Filter Tickets',
    }
    context = {
        'meta': meta,
        'form': form,
        'queryset': queryset,
    }
    return render(request, 'tickets/filter-tickets.html', context)
