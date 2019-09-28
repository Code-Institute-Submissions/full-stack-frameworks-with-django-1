from django.shortcuts import render

"""
    View for the homepage of the web app
"""
def home_view(request):
    meta = {
        'title': 'Issue Tracker',
    }
    context = {
        'meta': meta,
    }
    return render(request, 'pages/home_view.html', context)