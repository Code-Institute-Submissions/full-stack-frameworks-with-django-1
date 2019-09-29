from django.shortcuts import render
from bugs.models import Bug

def home_view(request):
    """
        View for the homepage of the web app
    """
    meta = {
        'title': 'Issue Tracker',
    }
    context = {
        'meta': meta,
        'critical_bugs': Bug.objects.filter(priority='CRITICAL')[:2],
        'high_bugs': Bug.objects.filter(priority='HIGH')[:2],
        'medium_bugs': Bug.objects.filter(priority='MEDIUM')[:2],
        'low_bugs': Bug.objects.filter(priority='LOW')[:2],
    }
    return render(request, 'pages/home_view.html', context)