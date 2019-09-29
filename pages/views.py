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
