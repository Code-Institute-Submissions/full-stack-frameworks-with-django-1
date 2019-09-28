from django.shortcuts import render

def home_view(request):
    """
        View for the homepage of the web app
    """
    meta = {
        'title': 'Issue Tracker',
    }
    context = {
        'meta': meta,
    }
    return render(request, 'pages/home_view.html', context)