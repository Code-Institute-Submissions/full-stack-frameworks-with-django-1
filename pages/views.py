from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bugs.models import Bug


def home_view(request):
    """
        View for the homepage of the web app
        that pulls in recent bugs
    """
    meta = {
        'title': 'Issue Tracker',
    }
    bugs = {
        'critical': Bug.objects.filter(priority='CRITICAL', status='IP')[:2],
        'high': Bug.objects.filter(priority='HIGH', status='IP')[:2],
        'medium': Bug.objects.filter(priority='MEDIUM', status='IP')[:2],
        'low': Bug.objects.filter(priority='LOW', status='IP')[:2],
    }
    context = {
        'meta': meta,
        'bugs': bugs,
    }
    return render(request, 'pages/home_view.html', context)


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
    return render(request, 'pages/terms_view.html', context)


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
    return render(request, 'pages/refund_view.html', context)


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
    return render(request, 'pages/privacy_view.html', context)
