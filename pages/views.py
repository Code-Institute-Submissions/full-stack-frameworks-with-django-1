from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket


def home_view(request):
    """
        View for the homepage of the web app
        that pulls in recent tickets
    """
    meta = {
        'title': 'Issue Tracker',
    }
    tickets = {
        'critical': Ticket.objects.filter(priority='CRITICAL', status='IP')[:2],
        'high': Ticket.objects.filter(priority='HIGH', status='IP')[:2],
        'medium': Ticket.objects.filter(priority='MEDIUM', status='IP')[:2],
        'low': Ticket.objects.filter(priority='LOW', status='IP')[:2],
    }
    context = {
        'meta': meta,
        'tickets': tickets,
    }
    return render(request, 'pages/home-view.html', context)


def terms_and_conditions_view(request):
    """
        View for the refund policy as is required
        on an e-commerce store
    """
    meta = {
        'title': 'Terms & Conditions',
    }
    context = {
        'meta': meta,
    }
    return render(request, 'pages/terms-view.html', context)


def refund_policy_view(request):
    """
        View for the T&C's as is required
        on an e-commerce store
    """
    meta = {
        'title': 'Refund Policy',
    }
    context = {
        'meta': meta,
    }
    return render(request, 'pages/refund-view.html', context)


def privacy_policy_view(request):
    """
        View for the privacy policy as is required
        on an e-commerce store
    """
    meta = {
        'title': 'Privacy Policy',
    }
    context = {
        'meta': meta,
    }
    return render(request, 'pages/privacy-view.html', context)
